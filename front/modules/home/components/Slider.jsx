import React, { useRef, useState } from "react";
// Import Swiper React components
import { Swiper, SwiperSlide } from "swiper/react";

// Import Swiper styles
import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";

import "./styles.css";

// import required modules
import { Autoplay, Pagination, Navigation } from "swiper/modules";

export default function Slider() {
  return (
    <div className="select-none laptop:h-[300px] desktop:h-[450px] mobile:h-[180px] ">
      <Swiper
        spaceBetween={30}
        centeredSlides={true}
        loop={true}
        autoplay={{
          delay: 2500,
          disableOnInteraction: false,
        }}
        pagination={{
          clickable: true,
        }}
        navigation={true}
        modules={[Autoplay, Pagination, Navigation]}
        className="mySwiper"
      >
        <SwiperSlide>
          {/* <Image src="https://dkstatics-public.digikala.com/digikala-adservice-banners/814735a2338ecd27255a059a565d32f568db51b9_1757839171.jpg?x-oss-process=image/quality,q_95/format,webp" /> */}
          <img className="w-full h-full object-cover" src="https://dkstatics-public.digikala.com/digikala-adservice-banners/814735a2338ecd27255a059a565d32f568db51b9_1757839171.jpg?x-oss-process=image/quality,q_95/format,webp" alt="" />
        </SwiperSlide>
        <SwiperSlide>
            <img className="w-full h-full object-cover" src="https://dkstatics-public.digikala.com/digikala-adservice-banners/5632b401ae92891681ebf45d8e35f1ad5cb88b84_1757428776.gif?x-oss-process=image?x-oss-process=image/format,webp" alt="" />
        </SwiperSlide>
        <SwiperSlide>
            <img className="w-full h-full object-cover" src="https://dkstatics-public.digikala.com/digikala-adservice-banners/c09380a212a3a330ef7434da576afa0ab806c019_1757776456.jpg?x-oss-process=image/quality,q_95/format,webp" alt="" />
        </SwiperSlide>
        <SwiperSlide>
            <img className="w-full h-full object-cover" src="https://dkstatics-public.digikala.com/digikala-adservice-banners/3f1dd7eda8277aa2d5e9749e926f6b5be307f40c_1755005176.jpg?x-oss-process=image/quality,q_95/format,webp" alt="" />
        </SwiperSlide>
        <SwiperSlide>
            <img className="w-full h-full object-cover" src="https://dkstatics-public.digikala.com/digikala-adservice-banners/46004afd66f022e49f85223d44a5d27ef6bdc258_1757221804.jpg?x-oss-process=image/quality,q_95/format,webp" alt="" />
        </SwiperSlide>
        <SwiperSlide>
            <img className="w-full h-full object-cover" src="https://dkstatics-public.digikala.com/digikala-adservice-banners/3cf199865473647d82761a71c6153d0d765c88f0_1754829711.jpg?x-oss-process=image/quality,q_95/format,webp" alt="" />
        </SwiperSlide>
        <SwiperSlide>
            <img className="w-full h-full object-cover" src="https://dkstatics-public.digikala.com/digikala-adservice-banners/efff3e736a93826d87156b51a8e7e63678d5b7a9_1757750447.jpg?x-oss-process=image/quality,q_95/format,webp" alt="" />
        </SwiperSlide>
        <SwiperSlide>
            <img className="w-full h-full object-cover" src="https://dkstatics-public.digikala.com/digikala-adservice-banners/a4dfa1d8de1d8a0a47eebc5318678c5e1bbf3c50_1757772475.jpg?x-oss-process=image/quality,q_95/format,webp" alt="" />
        </SwiperSlide>
        <SwiperSlide>
            <img className="w-full h-full object-cover" src="https://dkstatics-public.digikala.com/digikala-adservice-banners/df453a7ef29220b171ad42e0a28b26e0f01d8719_1757754443.jpg?x-oss-process=image/quality,q_95/format,webp" alt="" />
        </SwiperSlide>
      </Swiper>
    </div>
  );
}
