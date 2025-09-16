'use client'

import { useEffect, useState } from "react";

const Hero = () => {
    const [theme, setTheme] = useState('light'); // مقدار اولیه اضافه شد
    
    useEffect(() => {
        // فقط در سمت کلاینت اجرا شود
        if (typeof window !== 'undefined') {
            const savedTheme = localStorage.getItem('theme');
            const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            
            if (savedTheme) {
                setTheme(savedTheme);
            } else if (systemPrefersDark) {
                setTheme('dark');
            }
        }
    }, []);

    useEffect(() => {
        // فقط در سمت کلاینت اجرا شود
        if (typeof window !== 'undefined') {
            const html = document.documentElement;
            html.setAttribute('data-theme', theme);
            localStorage.setItem('theme', theme);
        }
    }, [theme]);

    const toggleTheme = () => {
        setTheme(theme === 'light' ? 'dark' : 'light');
    };

    return ( 
        <>
                <button 
                    onClick={toggleTheme} 
                    aria-label={`Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`} 
                    className="w-[35px] h-[35px]  cursor-pointer flex justify-center items-center  rounded-full bg-gray-200 hover:bg-gray-300 dark:hover:bg-gray-600 dark:bg-gray-700 transition-colors duration-200"
                >
                {theme === 'dark' ? (
                    // آیکون خورشید برای حالت تاریک
                    <svg className="w-6 h-6 text-yellow-300" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 01-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clipRule="evenodd" />
                    </svg>
                ) : (
                    // آیکون ماه برای حالت روشن
                    <svg className="w-6 h-6 text-gray-700" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z" />
                    </svg>
                )}
                </button>
        </>
    );
}

export default Hero;