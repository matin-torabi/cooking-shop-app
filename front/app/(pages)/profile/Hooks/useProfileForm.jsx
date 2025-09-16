"use client";

import useUpdateToken from "@/app/Hook/useUpdateToken";
import { url } from "@/app/settings/settings";
import axios from "axios";
import { getCookie, setCookie } from "cookies-next";
import { useFormik } from "formik";
import { toast } from "react-toastify";
import * as yup from "yup";

const postInformation = (values) => {
  const access = getCookie("access");

  axios
    .post(
      `${url}/profile/complete/`,
      {
        first_name: values.first_name,
        last_name: values.last_name,
      },
      {
        headers: {
          Authorization: `Bearer ${access}`,
          "Content-Type": "application/json",
        },
      }
    )
    .then((response) => {
      console.log(response.data);
      showToastMessage(response.data.message);
      useUpdateToken(response.status);
    })
    .catch((error) => {
      if (error.response && error.response.status === 401) {
        const refresh = getCookie("refresh");

        axios
          .post(`${url}/auth/token/refresh/`, { refresh: refresh })
          .then((refreshResponse) => {
            const newAccess = refreshResponse.data.access;
            setCookie("access", newAccess);
            console.log("New access token:", newAccess);

            return axios.post(
              `${url}/profile/complete/`,
              {
                first_name: values.first_name,
                last_name: values.last_name,
              },
              {
                headers: {
                  Authorization: `Bearer ${newAccess}`,
                  "Content-Type": "application/json",
                },
              }
            );
          })
          .then((retryResponse) => {
            console.log(retryResponse.data);
            showToastMessage(retryResponse.data.message);
          })
          .catch((refreshError) => {
            console.error("Refresh failed:", refreshError);
            showToastErrorMessage("لطفا ابتدا وارد حساب خود شوید");
          });
      } else {
        console.error(error);
        showToastErrorMessage(error.message);
      }
    });
};

const showToastMessage = (suc) => {
  toast.success(suc, {
    position: "top-right",
  });
};

const showToastErrorMessage = (err) => {
  toast.error(err, {
    position: "top-right",
  });
};

export default function useProfileForm() {
  const nameSchema = yup.object().shape({
    first_name: yup
      .string()
      .trim()
      .required("نام را وارد کنید")
      .min(2, "First name must be at least 2 characters")
      .max(50, "First name must be at most 50 characters"),
    last_name: yup
      .string()
      .trim()
      .min(2, "First name must be at least 2 characters")
      .max(50, "First name must be at most 50 characters")
      .required("نام خانوادگی را وارد کنید"),
  });

  const formik = useFormik({
    initialValues: {
      first_name: "",
      last_name: "",
    },
    validationSchema: nameSchema,
    onSubmit: async (values) => {
      postInformation(values);
    },
  });

  return formik;
}
