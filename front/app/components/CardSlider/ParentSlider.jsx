import Link from "next/link";
import CardSlider from "./CardSlider";
import { FaArrowLeft } from "react-icons/fa";

const ParentSlider = () => {
  return (
    <>
      <section className="mobile:w-full laptop:w-[95%] rounded-2xl desktop:w-[70%] flex flex-col items-center justify-center mx-auto h-[390px] my-[140px] p-5 dark:bg-[#191E24] bg-[#FE5F55] ">
        <div className="w-full h-[12%] flex justify-between text-white">
          <h1 className="text-xl font-[Yekan]">دوره های آموزشی</h1>
          <Link href="products" className="flex gap-2 justify-center">
            <span className="text-sm font-[Yekan]">مشاهده همه</span>
            <FaArrowLeft />
          </Link>
        </div>
        <div className="w-full h-[88%] ">
          <CardSlider />
        </div>
      </section>
    </>
  );
};

export default ParentSlider;
