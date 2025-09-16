import Link from 'next/link';
import React from 'react';
import { AiFillGithub } from 'react-icons/ai';
import { FaLinkedin, FaTelegram, FaWhatsapp } from 'react-icons/fa';

const Footer = () => {
  return (
    <footer dir='ltr' className="gradient-bg text-[#E1EEBC] bg-[#328E6E] py-8 px-4">  
      <div className="container mx-auto max-w-6xl">
        <div className="flex flex-col tablet:flex-row items-center justify-between">
          <div className="flex items-center mb-6 tablet:mb-0">
            <div className="relative">
              <img
                src="/public/image/profile.jpg"
                alt="Profile"
                className="w-24 h-24 object-cover rounded-full border-4 border-white shadow-lg profile-img"
              />
              {/* <span className="absolute bottom-0 right-0 bg-[#328E6E] text-white rounded-full px-2 py-1 text-xs font-bold">
                React
              </span> */}
            </div>
            <div className="ml-4 text-[#ECE3CE]">
              <h2 className="text-xl font-bold">Matin Torabi</h2>
              <p className="text-sm mt-1">Frontend Developer</p>
            </div>
          </div>

          {/* Social Media Links */}
          <div className="flex space-x-4">
            <Link
              href="/"
              className="social-icon bg-white text-[#328E6E] w-12 h-12 rounded-full flex items-center justify-center transition-all duration-300 hover:bg-[#E1EEBC] shadow-lg"
            >
                <FaTelegram className='text-2xl' />
            </Link>   
            <Link
              href="/"
              className="social-icon bg-white text-[#328E6E] w-12 h-12 rounded-full flex items-center justify-center transition-all duration-300 hover:bg-[#E1EEBC] shadow-lg"
            >
                <FaLinkedin className='text-2xl' />
            </Link>                        
            <Link
              href="/"
              className="social-icon bg-white text-[#328E6E] w-12 h-12 rounded-full flex items-center justify-center transition-all duration-300 hover:bg-[#E1EEBC] shadow-lg"
            >
                <FaWhatsapp className='text-2xl' />
            </Link>         
            <Link
              href="/"
              className="social-icon bg-white text-[#328E6E] w-12 h-12 rounded-full flex items-center justify-center transition-all duration-300 hover:bg-[#E1EEBC] shadow-lg"
            >
                <AiFillGithub className='text-2xl' />
            </Link>                     
          </div>
        </div>

        {/* Additional Info */}
        <div className="mt-8 grid grid-cols-1 tablet:grid-cols-3 gap-8 text-center tablet:text-left">
          <div>
            <h3 className="font-bold text-lg mb-2">About Me</h3>
            <p className="text-sm">
              Frontend developer specialized in React and modern web technologies.
            </p>
          </div>
          <div>
            <h3 className="font-bold text-lg mb-2">Contact Info</h3>
            <p className="text-sm">sajjad.torabi95@gmail.com</p>
            <p className="text-sm">+98 903 325 9308</p>
          </div>
          <div>
            <h3 className="font-bold text-lg mb-2">Location</h3>
            <p className="text-sm">Tehran Gharb, Kan</p>
          </div>
        </div>

        {/* Copyright Text */}
        <div className="mt-8 pt-6 border-t border-white/30 text-[#DDF4E7] text-center">
          <p>
            © 2025 Made By <span className="font-bold">Matin Torabi</span>
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
