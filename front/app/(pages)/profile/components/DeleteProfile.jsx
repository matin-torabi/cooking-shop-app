"use client";
import useUpdateToken from "@/app/Hook/useUpdateToken";
import { url } from "@/app/settings/settings";
import axios from "axios";
import { getCookie } from "cookies-next";
import { useEffect, useRef, useState } from "react";
import { IoMdClose } from "react-icons/io";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const DeleteProfile = ({ openProfile, setOpenProfile }) => {
  const fileInputRef = useRef(null);
  const [preview, setPreview] = useState('http://192.168.70.237:8000/media/ananymouse/ananymouse.jpg/');
  const [file, setFile] = useState(null);
  const [select, setSelect] = useState(false);
  

  const handleButtonClick = () => {
    fileInputRef.current.click(); // وقتی روی دکمه می‌زنیم input مخفی فعال می‌شود
  };

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
      setPreview(URL.createObjectURL(selectedFile)); 
      setFile(selectedFile); 
      setSelect(true);
    }
  };

  const handleDeleteProfile = () => {
    const access = getCookie("access");

    axios
      .delete(`${url}/profile/delete/`, {
        headers: {
          Authorization: `Bearer ${access}`,
          "Content-Type": "application/json",
        },
      })
      .then((response) => {
        console.log("Deleted:", response.data.message);
        showToastMessage(response.data.message);
        setOpenProfile(false);
        useUpdateToken(response.status)
        // ✅ کمی تاخیر بذار تا Toast نمایش داده بشه بعد رفرش
        setTimeout(() => {
          window.location.reload();
        }, 1500);
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
  };

  const handleSendProfile = () => {
    if (!file) return; // فقط وقتی فایل جدید انتخاب شد
    const access = getCookie("access");
    const formData = new FormData();
    formData.append("image", file);

    axios
      .patch(`${url}/profile/update/`, formData, {
        headers: {
          Authorization: `Bearer ${access}`,
          "Content-Type": "multipart/form-data",
        },
      })
      .then((response) => {
        console.log("Profile image updated:", response.data);
        showToastMessage(response.data.message);
        // alert(response.data.message)
        setOpenProfile(false);
        window.location.reload();
        useUpdateToken(response.status)
      })
      .catch((error) => {
        console.log(error);
      });
  };

  //   useEffect(() => {
  //     if (!file) return; // فقط وقتی فایل جدید انتخاب شد

  //     const access = getCookie("access");

  //     const formData = new FormData();
  //     formData.append("image", file);

  //     axios
  //       .post(`${url}/profile/update/`, formData, {
  //         headers: {
  //           Authorization: `Bearer ${access}`,
  //           "Content-Type": "multipart/form-data",
  //         },
  //       })
  //       .then((response) => {
  //         console.log("Profile image updated:", response.data);
  //         showToastMessage(response.data.message);
  //         // alert(response.data.message)
  //       })
  //       .catch((error) => {
  //         console.error(
  //           "Error updating image:",
  //           error.response?.data || error.message
  //         );
  //       });
  //     setTimeout(() => {
  //       setOpenProfile(false);
  //     }, 3000);
  //   }, [file]);

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
      {openProfile && (
        <div
          className="fixed font-[Yekan] inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm"
          onClick={() => setOpenProfile(false)} // بستن با کلیک روی بک‌دراپ
        >
          <div
            className="animate-fadeInScale bg-white dark:bg-[#242424] rounded-xl shadow-2xl p-6 h-[380px] mobile:w-[300px] tablet:w-[350px] relative"
            onClick={(e) => e.stopPropagation()} // جلوگیری از بستن مودال با کلیک داخل آن
          >
            {/* ضربدر بالای مودال */}
            <button
              onClick={() => setOpenProfile(false)}
              className="absolute top-4 right-4 text-gray-400 hover:text-gray-600 dark:text-[#e3e3e3] dark:hover:text-[#9e9e9e] transition text-lg font-bold"
            >
              <IoMdClose className="text-2xl cursor-pointer" />
            </button>
            <div className="mt-8 flex justify-center mobile:w-[200px] tablet:w-[300px] h-[250px]">
              {preview && (
                <img
                  src={preview}
                  alt=""
                  className="w-full h-full object-cover"
                />
              )}
              <input
                type="file"
                accept="image/*"
                ref={fileInputRef}
                className="hidden"
                onChange={handleFileChange}
              />
            </div>
            <div className="flex justify-end gap-3 mt-5">
              <button
                onClick={handleDeleteProfile}
                className="px-4 py-2 rounded-lg cursor-pointer duration-300 border border-gray-300 text-gray-600 dark:text-[#e3e3e3] dark:hover:text-gray-600 hover:bg-gray-100 transition-all text-sm"
              >
                حذف
              </button>
              {select ? (
                <button
                  onClick={handleSendProfile}
                  className="px-4 py-2 rounded-lg cursor-pointer duration-300 bg-[#E4004B] text-white hover:bg-[#e4004cc9] transition-all text-sm shadow"
                >
                  افزودن
                </button>
              ) : (
                <button
                  onClick={handleButtonClick}
                  className="px-4 py-2 rounded-lg cursor-pointer duration-300 bg-[#E4004B] text-white hover:bg-[#e4004cc9] transition-all text-sm shadow"
                >
                  انتخاب
                </button>
              )}
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default DeleteProfile;
