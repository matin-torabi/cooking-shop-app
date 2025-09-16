"use client";
import useUpdateToken from "@/app/Hook/useUpdateToken";
import { url } from "@/app/settings/settings";
import axios from "axios";
import { deleteCookie, getCookie } from "cookies-next";
import { useRouter } from "next/navigation";
import { IoMdClose } from "react-icons/io";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const LogoutModal = ({ open, setOpen }) => {
  const router = useRouter();

  const logout = () => {
    const access = getCookie("access");
    const refresh = getCookie("refresh");

    axios
      .delete(`${url}/auth/logout/`, {
        headers: {
          Authorization: `Bearer ${access}`,
          "Content-Type": "application/json",
        },
        data: {
          refresh: refresh,
        },
      })
      .then((response) => {
        console.log("Deleted:", response.data.message);
        showToastMessage(response.data.message);
        deleteCookie("access");
        deleteCookie("refresh");
        useUpdateToken(response.status)
      })
      .catch((error) => {
        if (error.response) {
          console.log("Server error:", error.response.data);
          showToastErrorMessage(error.response.data.message);
        } else if (error.request) {
          console.log("No response from server:", error.request);
          showToastErrorMessage(error.request);
        } else {
          console.log("Request setup error:", error.message);
          showToastErrorMessage(error.message);
        }
      });
    setOpen(false);
    router.push("/login");
  };

  const showToastMessage = (suc) => {
    toast.success(suc, {
      position: "top-right",
    });
  };

  const showToastErrorMessage = (err) => {
    toast.error(err, {
      position: "top-right",
    });
  };

  return (
    <>
      <ToastContainer autoClose={1000} toastClassName="font-[Yekan]" />

      {open && (
        <div
          className="fixed font-[Yekan] inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm"
          onClick={() => setOpen(false)} // بستن با کلیک روی بک‌دراپ
        >
          <div
            className="animate-fadeInScale bg-white dark:bg-[#242424] rounded-xl shadow-2xl p-6 h-[200px] mobile:w-[350px] tablet:w-[400px] relative"
            onClick={(e) => e.stopPropagation()} // جلوگیری از بستن مودال با کلیک داخل آن
          >
            {/* ضربدر بالای مودال */}
            <button
              onClick={() => setOpen(false)}
              className="absolute top-4 right-4 text-gray-400 hover:text-gray-600 dark:text-[#e3e3e3] dark:hover:text-[#9e9e9e] transition text-lg font-bold"
            >
              <IoMdClose className="text-2xl cursor-pointer" />
            </button>

            <h2 className="text-[16px] font-bold text-gray-800 dark:text-[#e3e3e3] mb-3 pt-8 flex items-center gap-2">
              خروج از حساب کاربری
            </h2>
            <p className="text-[#9e9e9e] mb-8 mobile:text-sm tablet:text-[16px]">
              مطمئنی می‌خوای از حساب کاربری خارج بشوی؟
            </p>
            <div className="flex justify-end gap-3">
              <button
                onClick={() => setOpen(false)}
                className="px-4 py-2 rounded-lg cursor-pointer duration-300 border border-gray-300 text-gray-600 dark:text-[#e3e3e3] dark:hover:text-gray-600 hover:bg-gray-100 transition-all text-sm"
              >
                انصراف
              </button>
              <button
                onClick={logout}
                className="px-4 py-2 rounded-lg cursor-pointer duration-300 bg-[#E4004B] text-white hover:bg-[#e4004cc9] transition-all text-sm shadow"
              >
                بله، خارج شو
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default LogoutModal;
