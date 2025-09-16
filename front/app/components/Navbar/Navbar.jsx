"use client";

import { RiShoppingBasketLine } from "react-icons/ri";
import Link from "next/link";
import { BiSearch } from "react-icons/bi";
import { IoMenu } from "react-icons/io5";
import { HiOutlineLogin } from "react-icons/hi";
import { FaHouse } from "react-icons/fa6";
import { useContext, useEffect, useState } from "react";
import Hero from "../Hero/Hero";
import axios from "axios";
import { getCookie, setCookie } from "cookies-next";
import { url } from "@/app/settings/settings";
import useUpdateToken from "@/app/Hook/useUpdateToken";


// function getProfile(setProfile, setimage_url, setcart_count) {
//   const refresh = getCookie("refresh");
//   const access = getCookie("access");
//   axios
//     .get(`${url}/profile/navbar/`, {
//       headers: {
//         Authorization: `Bearer ${access}`,
//         "Content-Type": "application/json",
//       },
//     })
//     .then((response) => {
//       console.log(response.data);
//       setStatu(response.status);
//       if (response.status === 200) {
//         setProfile(true);
//       }
//       setimage_url(response.data.user.profile_image);
//       setcart_count(response.data.user.cart_count);
//       console.log(response.data.user.cart_count);
//       console.log(response.data.user.profile_image);
//     })
//     .catch(async (error) => {
//       if (error.response) {
//         if (error.response.status === 401) {
//           try {
//             const refreshResponse = await axios.post(
//               `${url}/auth/token/refresh/`,
//               {
//                 refresh: refresh,
//               }
//             );
//             if (refreshResponse.status === 200) {
//               setCookie("refresh", refreshResponse.data.refresh);
//               setCookie("access", refreshResponse.data.access);
//               console.log(refreshResponse.data.refresh);
//               console.log(refreshResponse.data.access);
//             }
//           } catch (refreshError) {
//             console.error(refreshError);
//           }
//         }
//       }
//       console.error(error);
//     });
// }
async function getProfile(setProfile, setimage_url, setcart_count) {
  try {
    const refresh = getCookie("refresh");
    let access = getCookie("access");

    // درخواست اولیه پروفایل
    let response = await axios.get(`${url}/profile/navbar/`, {
      headers: {
        Authorization: `Bearer ${access}`,
        "Content-Type": "application/json",
      },
    });

    // موفقیت‌آمیز
    if (response.status === 200) {
      setProfile(true);
      setimage_url(response.data.user.profile_image);
      setcart_count(response.data.user.cart_count);
      console.log(response.data.user.profile_image, response.data.user.cart_count);
    }
  } catch (error) {
    // اگر 401 بود، یعنی توکن منقضی شده
    if (error.response && error.response.status === 401) {
      try {
        const refresh = getCookie("refresh");
        const refreshResponse = await axios.post(`${url}/auth/token/refresh/`, {
          refresh: refresh,
        });

        if (refreshResponse.status === 200) {
          // کوکی‌ها رو آپدیت کن
          setCookie("refresh", refreshResponse.data.refresh);
          setCookie("access", refreshResponse.data.access);
          access = refreshResponse.data.access;

          // دوباره درخواست پروفایل با توکن جدید
          const profileResponse = await axios.get(`${url}/profile/navbar/`, {
            headers: {
              Authorization: `Bearer ${access}`,
              "Content-Type": "application/json",
            },
          });

          setProfile(true);
          setimage_url(profileResponse.data.user.profile_image);
          setcart_count(profileResponse.data.user.cart_count);
          console.log(profileResponse.data.user.profile_image, profileResponse.data.user.cart_count);
        }
      } catch (refreshError) {
        console.error("Refresh token error:", refreshError);
      }
    } else {
      console.error("Profile fetch error:", error);
    }
  }
}

const Navbar = () => {
  const [show, setShow] = useState(false);
  const [profile, setProfile] = useState(false);
  const [image_url, setimage_url] = useState("");
  const [cart_count, setcart_count] = useState(0);

  const toggleVisibility = () => {
    setShow(!show);
  };
  useEffect(() => {
    getProfile(setProfile, setimage_url, setcart_count);
  }, []);

  return (
    <>
      <header className="sticky dark:border-b-[#ffffffde] dark:border-b-[1px] top-0 left-0 z-[50] mobile:bg-[#e2e2e2] laptop:bg-white w-[100%] dark:bg-[#1A1A1A] desktop:px-0 mobile:px-[20px] mobile:h-[60px] laptop:h-[100px] flex items-center justify-center shadow-md">
        <div className="mobile:w-full laptop:w-[1240px] h-full flex laptop:flex-col mobile:flex-row">
          <div className="w-full h-full flex mobile:items-center laptop:items-start justify-between">
            <div className="mobile:w-full laptop:w-[80%] h-full flex items-center mobile:justify-between laptop:justify-start mobile:gap-0 laptop:gap-[30px]">
              <IoMenu
                onClick={toggleVisibility}
                className="text-2xl mobile:flex laptop:hidden cursor-pointer dark:text-[#e3e3e3]"
              />
              <div className="mobile:flex laptop:hidden">
                <Hero />
              </div>
              <div className="flex mobile:w-[321px] tablet:w-[571px] laptop:w-[371px] h-[40px] rounded-xl shadow bg-[#F7F8FA]">
                <div className="w-[30px] h-[40px] items-center justify-center flex">
                  <BiSearch className="text-2xl cursor-pointer opacity-30" />
                </div>
                <div className="w-[341px] h-[40px] flex items-center">
                  <input
                    type="search"
                    className="w-full text-[16px] font-[Yekan] outline-none text-[#757575] "
                    placeholder="جستجو محصولات"
                  />
                </div>
              </div>
              <div className="mobile:hidden laptop:flex w-[340px] h-[30px] justify-between items-center">
                <Link
                  href="/"
                  className="text-[14px] font-[Yekan] text-[#a3a3a3] hover:text-[#FE5F55] transition-all duration-200 ease-linear"
                >
                  خانه
                </Link>
                <Link
                  href="/course"
                  className="text-[14px] font-[Yekan] text-[#a3a3a3] hover:text-[#FE5F55] transition-all duration-200 ease-linear"
                >
                  دوره ها
                </Link>
                <Link
                  href="/products"
                  className="text-[14px] font-[Yekan] text-[#a3a3a3] hover:text-[#FE5F55] transition-all duration-200 ease-linear"
                >
                  محصولات
                </Link>
                <Link
                  href="/products"
                  className="text-[14px] font-[Yekan] text-[#a3a3a3] hover:text-[#FE5F55] transition-all duration-200 ease-linear"
                >
                  ارتباط ما
                </Link>
                <Link
                  href="/about"
                  className="text-[14px] font-[Yekan] text-[#a3a3a3] hover:text-[#FE5F55] transition-all duration-200 ease-linear"
                >
                  درباره ما
                </Link>
                <Hero />
              </div>
            </div>
            <div className="mobile:hidden laptop:flex laptop:w-[20%] h-full justify-end items-center gap-3">
              <Link href="/basket">
                <div className="h-[42px] shadow rounded-xl flex relative justify-center items-center text-[14px] bg-[#F7F8FA] font-[Yekan] text-white w-[42px] ">
                  <span className="cursor-pointer bg-[#FE5F55] absolute flex items-center justify-center rounded-full text-white w-[20px] mobile:top-[10px] h-[20px] laptop:top-[-5px] left-[30px] font-[Number]">
                    {cart_count}
                  </span>
                  <RiShoppingBasketLine className="text-3xl text-[#FE5F55] pt-1.5 hover:text-[#FE5F55] transition-all duration-200 ease-linear" />
                </div>
              </Link>
              {profile === false ? (
                <Link href="/login">
                  <div className="h-[42px] shadow rounded-xl flex justify-center items-center text-[14px] bg-[#FE5F55] font-[Yekan] text-white w-[103px] hover:bg-[#e24257] transition-all duration-300 ease-linear">
                    ورود و ثبت‌نام
                  </div>
                </Link>
              ) : (
                <Link href="/profile">
                  <div className=" shadow rounded-xl flex justify-center items-center font-[Yekan] text-white transition-all duration-300 ease-linear cursor-pointer">
                    <img
                      className="rounded-full object-cover w-[40px] h-[40px] "
                      src={image_url}
                      alt=""
                    />
                  </div>
                </Link>
              )}
            </div>
          </div>
        </div>
      </header>

      {show && (
        <div className="w-[30vh] z-50 absolute right-0 flex flex-col bg-[#e2e2e2]">
          <Link
            href="/"
            className="pr-5 py-2.5 hover:bg-white text-[14px] font-[Yekan] text-[#a3a3a3] hover:text-[#FE5F55] transition-all duration-200 ease-linear"
          >
            خانه
          </Link>
          <Link
            href="/course"
            className="pr-5 py-2.5 hover:bg-white text-[14px] font-[Yekan] text-[#a3a3a3] hover:text-[#FE5F55] transition-all duration-200 ease-linear"
          >
            دوره ها
          </Link>
          <Link
            href="/products"
            className="pr-5 py-2.5 hover:bg-white text-[14px] font-[Yekan] text-[#a3a3a3] hover:text-[#FE5F55] transition-all duration-200 ease-linear"
          >
            محصولات
          </Link>
          <Link
            href="/products"
            className="pr-5 py-2.5 hover:bg-white text-[14px] font-[Yekan] text-[#a3a3a3] hover:text-[#FE5F55] transition-all duration-200 ease-linear"
          >
            ارتباط ما
          </Link>
          <Link
            href="/about"
            className="pr-5 py-2.5 hover:bg-white text-[14px] font-[Yekan] text-[#a3a3a3] hover:text-[#FE5F55] transition-all duration-200 ease-linear"
          >
            درباره ما
          </Link>
        </div>
      )}

      <section className="w-full h-[60px] px-5 bg-[#e2e2e2] fixed left-0 bottom-0 z-50 mobile:flex laptop:hidden justify-center items-center dark:bg-[#1A1A1A] dark:border-t-[1px] dark:border-t-[#e3e3e3]">
        <div className="mobile:w-full tablet:w-[500px] flex justify-between items-center">
          <Link href="/">
            <div className="w-[42px] h-[42px] shadow rounded-xl flex justify-center items-center text-[14px] bg-[#F7F8FA] text-white ">
              <FaHouse className="text-xl text-[#FE5F55] hover:text-[#FE5F55] transition-all duration-200 ease-linear" />
            </div>
          </Link>
          <Link href="/basket">
            <div className="w-[42px] relative h-[42px] shadow rounded-xl flex justify-center items-center text-[14px] bg-[#F7F8FA] text-white ">
              <RiShoppingBasketLine className="text-2xl text-[#FE5F55] hover:text-[#FE5F55] transition-all duration-200 ease-linear" />
              <span className="cursor-pointer bg-[#FE5F55] absolute flex items-center justify-center rounded-full text-white w-[20px] top-[-2px] h-[20px] left-[30px] font-[Number]">
                0
              </span>
            </div>
          </Link>
          {profile === false ? (
            <Link href="/login">
              <div className="w-[42px] h-[42px] shadow rounded-xl flex justify-center items-center text-[14px] bg-[#F7F8FA] text-white ">
                <HiOutlineLogin className="text-2xl text-[#FE5F55] hover:text-[#FE5F55] transition-all duration-200 ease-linear" />
              </div>
            </Link>
          ) : (
            <Link href="/profile">
              <div className="h-[42px] shadow rounded-xl flex justify-center items-center font-[Yekan] text-white w-[42px] bg-white transition-all duration-300 ease-linear cursor-pointer">
                <img className="rounded-full" src={image_url} alt="" />
              </div>
            </Link>
          )}
        </div>
      </section>
    </>
  );
};

export default Navbar;
