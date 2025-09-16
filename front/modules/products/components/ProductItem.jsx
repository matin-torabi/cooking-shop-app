"use client";

import { url } from "@/app/settings/settings";
import { Pagination } from "antd";
import axios from "axios";
import Link from "next/link";
import { useEffect, useState } from "react";

const ProductItem = () => {
  const [product, setProduct] = useState([]);
  useEffect(() => {
    axios.get(`${url}/product/list/`).then((res) => {
      setProduct(res.data.results);
      console.log(res.data.results);
      console.log(res.data);
    });
  }, []);
  
  return (
    <>
      {product.map((item) => (
        <div
          key={item.id}
          className="bg-white font-[Yekan] rounded-xl shadow-lg overflow-hidden w-80 transition-transform duration-300 hover:scale-105"
        >
          <div className="relative">
            <img
              src={item.image}
              alt={item.name}
              className="w-full h-56 object-cover"
            />
          </div>
          <div className="p-5">
            <div className="flex justify-between items-center mb-3">
              <h3 className="text-lg font-bold text-gray-800 line-clamp-1">{item.name}</h3>
            </div>
            <p className="text-gray-600 text-sm mb-4 line-clamp-2">{item.description}</p>

            <div className="flex justify-between items-center mb-4">
              <div className="flex w-full justify-between h-[48px]">
                <div className="">
                  <span className="font-[Number] text-xl font-bold text-gray-900">
                    {item.final_price}
                  </span>
                  {item.discount != 0 && (
                    <span className="font-[Number] text-sm text-gray-500 line-through block">
                      {item.price}
                    </span>
                  )}
                </div>
                <div className="">  
                  {item.discount != 0 && (
                    <div className="w-[34px] h-[20px] rounded-[10px] bg-red-500 flex items-center justify-center ">
                      <span className="font-[Number] text-sm text-white">
                        {item.discount}%
                      </span>
                    </div>
                  )}
                </div>
              </div>
            </div>

            <div className="flex justify-between space-x-2 space-x-reverse">
              <Link href={`/products/${item.slug}`}>
                <button className="bg-[#FE5F55] flex items-center justify-center gap-3 cursor-pointer hover:bg-[#FE4F44] text-white py-2 px-4 rounded-lg flex-1 transition-colors duration-300">
                  <span>مشاهده محصول</span>
                </button>
              </Link>
            </div>
          </div>
        </div>
      ))}  
    </>
  );
};

export default ProductItem;
