"use client";
import { useEffect, useRef, useState } from "react";
import Navbar from "@/app/components/Navbar/Navbar";
import Tabs from "./components/Tabs";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import DeleteProfile from "./components/DeleteProfile";
// import { CheckLogin } from "@/app/page";

const profile = () => {
  const [openProfile, setOpenProfile] = useState(false);
  const [preview, setPreview] = useState(
    "	http://192.168.70.237:8000/media/ananymouse/ananymouse.jpg/"
  );
  // CheckLogin()
  return (
    <>
      <Navbar />
      <ToastContainer autoClose={1000} toastClassName="font-[Yekan]" />
      <DeleteProfile openProfile={openProfile} setOpenProfile={setOpenProfile}/>
      <section className="w-full font-[Yekan] mobile:px-5 mobile:mt-[60px] desktop:mt-[100px] desktop:px-0 flex items-center justify-center">
        <div className="mobile:w-full desktop:w-[60%] p-5 dark:bg-[#242424] dark:rounded-2xl">
          <div className="mobile:flex-col laptop:flex-row flex items-center mobile:gap-2.5 laptop:gap-5">
              <img
                src={preview}
                alt=""
                onClick={()=>setOpenProfile(true)}
                className="cursor-pointer mobile:w-23 mobile:h-23 laptop:w-32 laptop:h-32 rounded-full object-cover border-4 border-blue-100 shadow"
              />
            <div className="flex flex-col gap-2 items-center">
              <h2 className="mobile:text-xl laptop:text-2xl dark:text-[#e3e3e3] ">
                متین
              </h2>
              <h2 className="mobile:text-xs laptop:text-sm font-[Number] dark:text-[#e3e3e3]">
                09126772538
              </h2>
            </div>
          </div>
          <Tabs/>
        </div>
      </section>
    </>
  );
};

export default profile;
