import { useState } from "react";
import useProfileForm from "../Hooks/useProfileForm";
import LogoutModal from "./LogoutModal";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { IoLogInOutline } from "react-icons/io5";

const Tabs = () => {
  const [activeTab, setActiveTab] = useState("courses");
  const [open, setOpen] = useState(false);
  const [deleteAcount, setDeleteAcount] = useState(false);
  const formik = useProfileForm()
  const role = "admin";

  let tabs = [
    { id: "courses", title: "دوره‌های من", icon: "book-open" },
    { id: "settings", title: "تنظیمات", icon: "cog" },
    { id: "certificates", title: "گواهینامه‌ها", icon: "certificate" },
  ];

  if (role === "admin") {
    tabs = [
      ...tabs,
      { id: "users", title: "اضافه کردن محصول", icon: "book-open" },
      { id: "dore", title: "اضافه کردن دوره", icon: "cog" },
    ];
  }

  return (
    <>
      <LogoutModal setOpen={setOpen} open={open}/>
      <div className="mt-5 mb-[100px] overflow-hidden">
        {/* Tab Headers */}
        <div className="border-b border-gray-200 dark:border-none">
          <nav className="flex items-center justify-center">
            {tabs.map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`px-6 py-4 text-sm font-medium cursor-pointer border-b-2 whitespace-nowrap flex items-center ${
                  activeTab === tab.id
                    ? "border-[#E4004B] text-[#E4004B] dark:border-[#e3e3e3] dark:text-[#e3e3e3]"
                    : "border-transparent text-gray-500 hover:text-gray-700 dark:hover:text-[#ebebeb99] dark:text-[#ebebeb99]"
                }`}
              >
                <i className={`fas fa-${tab.icon} ml-2 `}></i>
                {tab.title}
              </button>
            ))}
          </nav>
        </div>

        {/* Tab Contents */}
        <div className="p-6">
          {/* Courses Tab */}
          {activeTab === "courses" && (
            <div>
              <h2 className="text-xl font-bold text-gray-800 mb-6 dark:text-[#e3e3e3]">
                دوره‌های خریداری شده
              </h2>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {/* Course Card 1 */}
                <div className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-xl p-6 border border-blue-200">
                  <div className="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center mb-4">
                    <svg
                      className="w-6 h-6 text-white"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C20.832 18.477 19.246 18 17.5 18c-1.746 0-3.332.477-4.5 1.253"
                      ></path>
                    </svg>
                  </div>
                  <h3 className="font-bold text-gray-800 mb-2">آموزش React</h3>
                  <p className="text-gray-600 text-sm mb-4">
                    یادگیری کامل React از صفر تا صد
                  </p>
                  <div className="flex justify-between items-center">
                    <span className="text-green-600 font-medium text-sm">
                      تکمیل شده
                    </span>
                    <button className="text-blue-600 hover:text-blue-800 text-sm font-medium">
                      ادامه دوره
                    </button>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Settings Tab */}
          {activeTab === "settings" && (
            <div>
              <h2 className="text-xl font-bold text-gray-800 mb-6 dark:text-[#e3e3e3]">
                تنظیمات حساب کاربری
              </h2>
              <div className="space-y-6">
                <form
                  onSubmit={formik.handleSubmit}
                  className="bg-gray-50 dark:bg-[#242424] dark:border-[1px] dark:border-[#ffffffde] rounded-xl p-6"
                >
                  <h3 className="font-semibold text-gray-800 mb-4 dark:text-[#e3e3e3]">
                    اطلاعات شخصی
                  </h3>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2 dark:text-[#e3e3e3]">
                        نام
                      </label>
                      <input
                        value={formik.values.first_name}
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                        name="first_name"
                        type="text"
                        className="w-full px-3 py-2 dark:text-[#e3e3e3] border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#FE5F55] focus:border-transparent "
                      />
                      {formik.touched.first_name &&
                        formik.errors.first_name && (
                          <p className="text-red-600 text-sm mt-2">
                            {formik.errors.first_name}
                          </p>
                        )}
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2 dark:text-[#e3e3e3]">
                        نام خانوادگی
                      </label>
                      <input
                        value={formik.values.last_name}
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                        name="last_name"
                        type="text"
                        className="w-full px-3 py-2 dark:text-[#e3e3e3] border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#FE5F55] focus:border-transparent "
                      />
                      {formik.touched.last_name && formik.errors.last_name && (
                        <p className="text-red-600 text-sm mt-2">
                          {formik.errors.last_name}
                        </p>
                      )}
                    </div>
                  </div>
                  <div className="flex justify-end mt-4">
                    <button
                      type="submit"
                      className="cursor-pointer text-sm flex items-center bg-[#FF714B] px-6 py-3 text-white font-semibold rounded-lg shadow-md hover:shadow-lg transition-all duration-300 hover:-translate-y-0.5"
                    >
                      ذخیره اطلاعات
                    </button>
                  </div>
                </form>
                <div className="bg-red-50 rounded-xl p-6 card dark:bg-[#242424] dark:border-[1px] dark:border-[#ffffffde]">
                  <h3 className="font-semibold text-[#E4004B] dark:text-[#FF748B] mb-4">
                    خروج از حساب کاربری
                  </h3>
                  <p className="text-[#E4004B] dark:text-[#FF748B] mb-4">
                    پس از خروج از حساب، برای دسترسی به پنل کاربری باید مجدداً
                    وارد شوید.
                  </p>
                    <button
                      onClick={() => setOpen(true)}
                      className="btn-exit bg-[#E4004B] dark:bg-[#FF748B] text-white px-6 py-2 rounded-lg flex items-center transition-colors cursor-pointer"
                    >
                      <IoLogInOutline className="text-xl" /> خروج از حساب کاربری
                    </button>
                </div>
              </div>
            </div>
          )}
          <ToastContainer autoClose={1000} toastClassName="font-[Yekan]" />
          {/* Certificates Tab */}
          {activeTab === "certificates" && (
            <div>
              <h2 className="text-xl font-bold text-gray-800 mb-6 dark:text-[#e3e3e3]">
                گواهینامه‌های دریافتی
              </h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="border-2 border-dashed border-gray-300 rounded-xl p-8 text-center">
                  <svg
                    className="w-16 h-16 text-gray-400 mx-auto mb-4"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"
                    ></path>
                  </svg>
                  <h3 className="text-lg font-semibold text-gray-800 mb-2">
                    گواهینامه React
                  </h3>
                  <p className="text-gray-600 mb-4">
                    تکمیل موفقیت‌آمیز دوره React
                  </p>
                  <button className="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg transition-colors">
                    دانلود گواهینامه
                  </button>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </>
  );
};

export default Tabs;
