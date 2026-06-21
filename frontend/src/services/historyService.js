import API from "./api";

export const getHistory = async () => {
  const token = localStorage.getItem("token");

  const res = await API.get("/api/history", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return res.data;
};

export const saveHistory = async (query) => {
  const token = localStorage.getItem("token");

  const res = await API.post(
    "/api/history",
    { query },
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return res.data;
};