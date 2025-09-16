'use client'
import "react-toastify/dist/ReactToastify.css";
import { useFormik } from "formik";
import Link from "next/link";
import { useEffect, useState } from "react";
import { GrLinkNext } from "react-icons/gr";
import getValidationSchema from "../getValidationSchema";
import axios from "axios";
import { url } from "@/app/settings/settings";
import { useRouter } from "next/navigation";
// import { loginContext } from "@/app/page";
import { useContext } from "react";
import { setCookie } from "cookies-next";
import { loginContext } from "@/app/page";
import { toast, ToastContainer } from "react-toastify";

// تابع ارسال شماره موبایل
async function sendPhone(phone, setResendTimer) {

  try {
    const response = await axios.post(`${url}/auth/register/step-one/`, {
      phone_number: phone
    });

    console.log(response.data);
    console.log(response.data.time);
    localStorage.setItem('temp_token', response.data.temp_token);

    // تنظیم تایمر بر اساس زمان باقی‌مانده سرور
    if (response.data.time) {
      setResendTimer(response.data.time); // مقدار واقعی از سرور
    } else {
      setResendTimer(120); // مقدار پیش‌فرض اگر سرور چیزی نفرستاد
    }

    return true; // ارسال موفق
  } catch (error) {
    if (error.response) {
      const errorMessage = error.response.data.message || error.response.data.detail || 'خطایی رخ داده است';
      alert(errorMessage);
      // showToastErrorMessage(errorMessage)
    } else if (error.request) {
      showToastErrorMessage("اتصال با سرور برقرار نشد")          
    } else {
      showToastErrorMessage("خطای ناشناخته رخ داده است")          
    }
    return false; // ارسال ناموفق
  }
}

const Register = () => {
  const [isStepTwo, setIsStepTwo] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [resendTimer, setResendTimer] = useState(0);

  const router = useRouter();

    useEffect(() => {
      let interval;
      if (resendTimer > 0) {
        interval = setInterval(() => {
          setResendTimer(prev => {
            if (prev <= 1) {
              clearInterval(interval);
              return 0;
            }
            return prev - 1;
          });
        }, 1000);
      }
      return () => clearInterval(interval);
    }, [resendTimer]);


  const formik = useFormik({
    initialValues: {
      phone: "",
      code: "",
    },
    validationSchema: getValidationSchema(isStepTwo),
    onSubmit: async (values) => {
      setIsSubmitting(true);

      if (!isStepTwo) {
        const success = await sendPhone(values.phone, setResendTimer);
        if (success) {
          setIsStepTwo(true); // فقط وقتی شماره موفق ارسال شد، مرحله دوم نمایش داده شود
        }
      } else {
        const temp_token = localStorage.getItem('temp_token');
        axios.post(`${url}/auth/register/step-two/`, {
          temp_token: temp_token,
          otp_code: values.code
        })
        .then(response => {
          // alert("ورود موفقیت‌آمیز ✅");
          showToastMessage()          
          setCookie("refresh", response.data.refresh);
          setCookie("access", response.data.access);    
          setTimeout(()=>{
            router.push("/");
          }, 1000)      
        })
        .catch(error => {
          console.error("خطا:", error);
          showToastErrorMessage("کد نادرست است")          
          // alert("کد نادرست است");
        });
      }

      setIsSubmitting(false);
    },
  });

  const handleResendCode = async () => {
    const phone = formik.values.phone;
    setIsSubmitting(true);
    await sendPhone(phone, setResendTimer);
    setIsSubmitting(false);
  };

  const showToastMessage = () => {
    toast.success("ورود موفقیت‌آمیز ✅", {
      position: "top-right"
    });
  };

  const showToastErrorMessage = (mes) => {
    toast.error(mes, {
      position: "top-right"
    });
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4 font-[Yekan]">
      <form
        onSubmit={formik.handleSubmit}
        className="font-[Number] w-full max-w-md bg-white rounded-lg shadow-md overflow-hidden"
      >
        {/* Header */}
        <div className="bg-[#E4004B] py-4 px-6">
          <div className="flex items-center">
            <Link href="/login">
              <GrLinkNext className="cursor-pointer text-[20px] text-white" />
            </Link>
            <h1 className="text-white text-xl font-bold text-center flex mx-auto">
              {/* عنوان دلخواه */}
            </h1>
          </div>
        </div>

        {/* Body */}
        <div className="p-6 space-y-6">
          <h2 className="text-gray-800 text-lg font-semibold text-center border-b pb-2">
            ثبت نام
          </h2>

          <div className="space-y-4">
            <p className="text-gray-600 text-sm">
              {isStepTwo
                ? "کد تأیید ارسال شده را وارد کنید"
                : "لطفا شماره موبایل خود را وارد کنید"}
            </p>
            <ToastContainer autoClose={1000}/>
            <div className="relative">
              {isStepTwo ? (
                <input
                  type="text"
                  name="code"
                  placeholder="کد تایید را وارد کنید"
                  value={formik.values.code}
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-[#FE5F55] focus:border-transparent"
                />
              ) : (
                <input
                  type="tel"
                  name="phone"
                  placeholder="شماره موبایل"
                  value={formik.values.phone}
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-[#FE5F55] focus:border-transparent"
                />
              )}
            </div>

            {/* خطاها */}
            {formik.touched.phone && formik.errors.phone && (
              <p className="text-red-600 text-sm">{formik.errors.phone}</p>
            )}
            {formik.touched.code && formik.errors.code && (
              <p className="text-red-600 text-sm">{formik.errors.code}</p>
            )}

            {/* دکمه‌ها */}
            {isStepTwo ? (
              <div className="flex flex-col space-y-3">
                <button
                  type="submit"
                  disabled={isSubmitting}
                  className="w-full bg-[#FE5F55] text-white py-2 px-4 rounded-md transition duration-200 focus:outline-none focus:ring-2 focus:ring-[#FE5F55] focus:ring-offset-2 disabled:opacity-70 disabled:cursor-not-allowed"
                >
                  {isSubmitting ? "در حال تأیید..." : "تأیید کد"}
                </button>

                <button
                  type="button"
                  onClick={handleResendCode}
                  disabled={resendTimer > 0 || isSubmitting}
                  className="w-full bg-gray-200 text-gray-700 py-2 px-4 rounded-md hover:bg-gray-300 transition duration-200 focus:outline-none focus:ring-2 focus:ring-gray-300 focus:ring-offset-2 disabled:opacity-70 disabled:cursor-not-allowed"
                >
                  {resendTimer > 0
                    ? `ارسال مجدد پس از ${resendTimer} ثانیه`
                    : "ارسال مجدد کد"}
                </button>
              </div>
            ) : (
              <button
                type="submit"
                disabled={isSubmitting}
                className="cursor-pointer w-full bg-[#E4004B] text-white py-2 px-4 rounded-md transition duration-200 focus:outline-none focus:ring-2 focus:ring-[#FE5F55] focus:ring-offset-2 disabled:opacity-70 disabled:cursor-not-allowed"
              >
                {isSubmitting ? "در حال ارسال..." : "دریافت کد تأیید"}
              </button>
            )}


          </div>
        </div>
      </form>
    </div>
  );
};

export default Register;
