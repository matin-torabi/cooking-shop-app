'use client'; 
import { BsArrowLeftCircle } from "react-icons/bs";
import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import 'swiper/css/navigation';
import { Navigation } from 'swiper/modules';
import { useEffect, useState } from 'react';
import Link from 'next/link';
import { LuClock } from 'react-icons/lu';
import { IoMdPerson } from 'react-icons/io';
import { FiArrowUpLeft } from 'react-icons/fi';

export default function CardSlider() {
  const [card, setCard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCard = async () => {
      try {
        const data = await useFetch.get('/card');
        setCard(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchCard();
  }, []);


  if (!card.length) return (
    <div className="flex justify-center items-center h-64">
      <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
    </div>
  );

  return (
    <Swiper
      breakpoints={{
        320: {
          slidesPerView: 2,
          spaceBetween: 5,
        },
        640: {
          slidesPerView: 4.5,
          spaceBetween: 5,
        },
        1100: {
          slidesPerView: 6.5,
          spaceBetween: 5,
        },
        1500: {
          slidesPerView: 5.5,
          spaceBetween: 5,
        },
      }}
      navigation={true}
      modules={[Navigation]}
      className="mySwiper w-full h-full"
    >
      {card.map((item) => (
        <SwiperSlide key={item.id} >
          <Link href={`/cors/${item.id}`} className="block h-full">
            <div className="font-[Yekan] flex flex-col gap-5 bg-white cursor-pointer dark:bg-[#1D232A] transition-shadow duration-300 overflow-hidden">
              <div className="w-full h-[150px] overflow-hidden">
                <img 
                  src={item.url}
                  alt={item.title || 'Course Image'} 
                  className="w-full h-full object-cover hover:scale-105 transition-transform duration-300"
                />
              </div>
              <div className="w-full flex flex-col gap-2.5 px-1 ">
                <p className="line-clamp-1 text-sm text-gray-800 dark:text-[#e3e3e3]">{item.body}</p>
                <div className="w-full h-[74px] border-y-gray-300 border-y-[1px] flex flex-col justify-center gap-2 py-2">
                  <div className="flex gap-3 items-center">
                    <LuClock className="text-xl opacity-70"/>
                    <span className="opacity-70 font-[Number] text-sm">{item.time}</span>
                  </div>
                  <div className="flex gap-3 items-center">
                    <IoMdPerson className="text-xl opacity-70"/>
                    <span className="text-sm font-[Yekan] opacity-70">{item.modares}</span>
                  </div>                        
                </div>
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    {item.offer && (
                      <span className="text-[#9e9e9e] text-sm font-[Number] line-through">{item.offer}</span>
                    )}
                    <div className="flex gap-1 items-center">
                      <span className="text-[#2b2b2b] text-[16px] font-[Number] dark:text-[#e3e3e3]">{item.price}</span>
                      <span className='text-[10px] pt-1'>تومان</span>
                    </div>
                  </div>
                  <FiArrowUpLeft className="text-xl text-[#FE5F55]"/>                     
                </div>
              </div>
            </div>
          </Link>
        </SwiperSlide>
      ))}
      <SwiperSlide className='mobile:hidden laptop:flex'>
        <div className="flex gap-3 flex-col items-center dark:bg-[#1D232A] justify-center w-full h-full">
          <Link href='/products' className="flex gap-3 flex-col items-center justify-center text-[#FE5F55]">
            <BsArrowLeftCircle className="text-6xl"/>
            <h1 className='font-[Yekan] text-sm'>مشاهده همه</h1>
          </Link>
        </div>
      </SwiperSlide>

    </Swiper>
  );
}