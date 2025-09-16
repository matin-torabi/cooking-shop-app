const { default: axios } = require("axios");
const { url } = require("../settings/settings");
const { getCookie, setCookie } = require("cookies-next");

export default function useUpdateToken(status) {
  const refresh = getCookie("refresh");
  // console.log(refresh);
  
  if (status === 401) {
    const response = axios.post(`${url}/auth/token/refresh/`, {
      refresh: refresh,
    });
    if (response.status === 200) {
        setCookie("refresh", response.data.refresh)
        setCookie("access", response.data.access)
        console.log(response.data.refresh);
        console.log(response.data.access);
    }
  }
}