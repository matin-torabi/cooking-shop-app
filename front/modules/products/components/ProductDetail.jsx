"use client";

import Navbar from "@/app/components/Navbar/Navbar";
import { url } from "@/app/settings/settings";
import axios from "axios";
import { useEffect, useState } from "react";
import { GoShareAndroid } from "react-icons/go";

const ProductDetail = ({ id }) => {
  const [count, setCount] = useState(0);
  const [i, setI] = useState(0);
  const [productDetails, setProductDetails] = useState([]);
  useEffect(() => {
    axios.get(`${url}/product/page/${id}/`).then((res) => {
      setProductDetails(res.data);
      console.log(`https://${window.location.host}/products/${id}/`);
      
    });
  }, []);

  return (
    <>
      <Navbar />
      <section className="mobile:w-full desktop:w-[1250px] mx-auto flex justify-center items-center my-[100px] ">
        <div className="w-[90%] relative flex mobile:flex-col gap-5 laptop:flex-row font-[Yekan] mobile:h-auto border-[1px] border-gray-300 p-5 rounded-xl shadow-2xl">
          <div className="w-full h-[400px] flex gap-5 flex-col items-center justify-center">
            <div className="w-[300px] h-[300px] rounded-xl cursor-pointer ">
              <img
                className="w-full h-full rounded-xl"
                src={productDetails?.image?.[i] || ""}
                alt=""
              />
            </div>
            <div className="mobile:w-full laptop:w-[60%] flex justify-center gap-3">
              {productDetails?.image?.map((imgSrc, index) => (
                <div
                  key={index}
                  onClick={() => setI(index)}
                  className="w-[100px] h-[100px] rounded-xl cursor-pointer hover:shadow-xl duration-300 border-[1px] border-gray-300"
                >
                  <img
                    className="w-full h-full rounded-xl object-cover"
                    src={imgSrc}
                  />
                </div>
              ))}
            </div>
          </div>
          <div className="w-full h-auto p-5 gap-5 flex flex-col ">
            <h1 className="text-xl ">{productDetails.name}</h1>
            <p className="text-sm text-justify text-gray-500 mobile:w-full laptop:w-[500px] leading-6">
              {productDetails.description}
            </p>
            <div className="border-t border-gray-200 pt-8">
              <h3 className="text-sm font-medium text-gray-900">
                مشخصات محصول
              </h3>
              <div className="mt-4 prose prose-sm text-gray-500">
                <ul className="space-y-2">
                  <li className="flex justify-between">
                    <span className="text-sm">وزن:</span>
                    <div className="flex gap-2">
                      <span className="font-medium text-sm text-gray-900">
                        {productDetails.weight_type}
                      </span>
                      <span className="font-medium font-[Number] text-sm text-gray-900">
                        {productDetails.weight}
                      </span>
                    </div>
                  </li>
                  <li className="flex justify-between">
                    <span className="text-sm">مدت نگهداری:</span>
                    <div className="flex gap-2">
                      <span className="font-medium text-sm text-gray-900">
                        {productDetails.shelf_life_type}
                      </span>
                      <span className="font-medium font-[Number] text-sm text-gray-900">
                        {productDetails.shelf_life}
                      </span>
                    </div>
                  </li>
                  {productDetails.discount != 0 && (
                    <li className="flex justify-between">
                      <span className="text-sm">قیمت اصلی :</span>
                      <span className="font-medium text-sm text-gray-500 line-through font-[Number]">
                        {productDetails.price}
                      </span>
                    </li>
                  )}
                  <li className="flex justify-between">
                    <span className="text-sm">قیمت نهایی :</span>
                    <span className="font-medium text-sm text-gray-900 font-[Number]">
                      {productDetails.final_price}
                    </span>
                  </li>
                  {productDetails.discount != 0 && (
                    <div className="w-[25px] absolute left-5 top-5 h-[25px] rounded-full bg-red-500 flex items-center justify-center ">
                      <span className="font-[Number] text-sm text-white">
                        {productDetails.discount}%
                      </span>
                    </div>
                  )}
                </ul>
              </div>
            </div>

            <div className="mt-8">
              <div className="flex items-center gap-4">
                <div className="flex items-center border border-gray-300 rounded-md">
                  <button
                    className="p-2 text-gray-600 hover:text-gray-900"
                    onClick={() =>
                      setCount((prev) => (prev > 0 ? prev - 1 : 0))
                    }
                  >
                    <svg
                      className="w-4 h-4 cursor-pointer"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M20 12H4"
                      ></path>
                    </svg>
                  </button>
                  <span
                    id="quantity"
                    className="px-4 font-[Number] py-2 text-gray-900 font-medium"
                  >
                    {count}
                  </span>
                  <button
                    className="p-2 text-gray-600 hover:text-gray-900"
                    onClick={() =>
                      setCount((prev) => (prev < 99 ? prev + 1 : 99))
                    }
                  >
                    <svg
                      className="w-4 h-4 cursor-pointer"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M12 4v16m8-8H4"
                      ></path>
                    </svg>
                  </button>
                </div>
                <button className="flex-1 bg-[#FE5F55] border border-transparent rounded-md py-3 px-8 flex items-center justify-center text-base font-medium text-white hover:bg-[#FE4F44] cursor-pointer focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                  افزودن به سبد خرید
                </button>
              </div>
            </div>

            <div className="mt-6 flex gap-4">
              <button className="cursor-pointer flex items-center justify-center px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50">
                <GoShareAndroid className="text-xl" />
                اشتراک‌گذاری
              </button>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default ProductDetail;
