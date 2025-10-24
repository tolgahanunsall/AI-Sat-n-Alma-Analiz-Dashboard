import React from "react";
import { createBrowserRouter, RouterProvider, Link, Outlet } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import UploadPage from "./pages/UploadPage";

function Layout() {
  return (
    <div>
      <nav className="bg-white border-b shadow-sm">
        <div className="max-w-6xl mx-auto px-4 py-3 flex gap-4">
          <Link to="/" className="font-semibold">Dashboard</Link>
          <Link to="/upload" className="font-semibold">Excel Yükle</Link>
        </div>
      </nav>
      <main className="max-w-6xl mx-auto">
        <Outlet />
      </main>
    </div>
  );
}

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      { index: true, element: <Dashboard /> },
      { path: "upload", element: <UploadPage /> },
    ],
  },
]);

export default function App() {
  return <RouterProvider router={router} />;
}
