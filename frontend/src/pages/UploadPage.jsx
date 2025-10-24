import React, { useState } from "react";
import { api } from "../api/client";

export default function UploadPage() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState(null);
  const [error, setError] = useState(null);

  const handleUpload = async () => {
    if (!file) return;
    try {
      const formData = new FormData();
      formData.append("file", file);
      const res = await api.post("/upload/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setSummary(res.data.summary);
      setError(null);
    } catch (e) {
      setError(e?.response?.data?.detail || "Yükleme hatası");
      setSummary(null);
    }
  };

  return (
    <div className="p-8">
      <h1 className="text-xl font-bold mb-4">Excel Yükle</h1>
      <input type="file" accept=".xls,.xlsx" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload} className="ml-4">
        <span className="button_top">Yükle</span>
      </button>
      {error && <div className="mt-4 text-red-600">{error}</div>}
      {summary && (
        <div className="mt-6 p-4 bg-gray-100 rounded-lg">
          <p>💰 Toplam Tutar: {summary.toplam_tutar?.toLocaleString()} ₺</p>
          <p>📅 Yıllık Ortalama: {summary.yillik_ortalama?.toLocaleString()} ₺</p>
          <p>🏢 En Büyük Tedarikçi: {summary.top_tedarikci}</p>
        </div>
      )}
    </div>
  );
}
