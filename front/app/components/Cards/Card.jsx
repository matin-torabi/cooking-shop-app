import { FiArrowUpLeft } from "react-icons/fi";
import { LuClock } from "react-icons/lu";
import { IoMdPerson } from "react-icons/io";
import Link from "next/link";

const Card = async () => {
  try {
    const res = await fetch('http://localhost:4000/card');
    
    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }
    
    const cards = await res.json();

    if (!cards || cards.length === 0) {
      return <div>No cards found</div>;
    }

    return (
      <>
        {cards.map((item) => (
          <Link key={item.id} href={`/cors/${item.id}`}>
            <div className="font-[Yekan] flex flex-col gap-5 border-[1px] border-gray-300 w-[265px] h-[439px] bg-white dark:bg-[#191E24] rounded-2xl cursor-pointer hover:shadow-2xl">
              <div className="w-full h-[233px]">
                <img src={item.url} alt="" className="w-full h-full rounded-t-2xl object-cover" />
              </div>
              <div className="w-full flex flex-col gap-5 px-3">
                <p className="line-clamp-1">{item.body}</p>
                <div className="w-full h-[80px] border-y-gray-300 border-y-[1px] flex flex-col justify-center gap-2">
                  <div className="flex gap-3">
                    <LuClock className="text-xl opacity-70"/>
                    <span className="opacity-70 font-[Number]">{item.time}</span>
                  </div>
                  <div className="flex gap-3">
                    <IoMdPerson className="text-xl opacity-70"/>
                    <span className="text-sm font-[Yekan] opacity-70">{item.modares}</span>
                  </div>                        
                </div>
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    <span className="text-[#9e9e9e] text-sm font-[Number]">{item.offer}</span>
                    <div className="flex gap-2.5">
                      <span className="text-[#2b2b2b] dark:text-[#ADB8BE] text-[16px] font-[Number]">{item.price}</span>
                      <img src='../../../public/image/Card/toman.svg' alt="" />
                    </div>
                  </div>
                  <FiArrowUpLeft className="text-xl text-[#FE5F55]"/>                     
                </div>
              </div>
            </div>                  
          </Link>                                                                                                             
        ))}
      </>
    );
  } catch (error) {
    console.error("Error fetching cards:", error);
    return <div>Error loading cards</div>;
  }
}

export default Card;