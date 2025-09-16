'use client'

import { createContext, useState } from "react";
import Navbar from "./components/Navbar/Navbar";
import HomeView from "@/modules/home/view/homeView";


export const loginContext = createContext()

// export function CheckLogin() {
//   const router = useRouter();

//   useEffect(() => {
//     const access = getCookie("access");
//     const refresh = getCookie("refresh");

//     if (!access && !refresh) {
//       redirect("/login");
//     }
//   }, [router]);

//   return null;
// }

export default function Home() {
  const [login, setLogin] = useState(false)
  // CheckLogin()

  return (
    <>
        <loginContext.Provider value={login} >
          <Navbar />
          {/* <div className="mobile:w-full desktop:w-[1920px] mx-auto block"> */}
            <HomeView/>
          {/* </div> */}
          {/* <Footer /> */}
        </loginContext.Provider>
    </>
  );
}
