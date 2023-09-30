// import './App.css'
import Login from "./pages/Login";
import Register from "./pages/Register";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import { BrowserRouter, Route, Routes, Outlet } from "react-router-dom";
import Footer from "./components/Footer";

export default function App() {
  return (
    <BrowserRouter>
      <div className="flex flex-col flex-wrap">
        <Navbar />
        <Outlet />
        <Routes>
          <Route path="/" element={<Home />} />
          {/* <Route path="/blog/*" element={<BlogApp />} /> */}
          {/* <Route path="/users/*" element={<UserApp />} /> */}
          <Route path="/login/*" element={<Login />} />
          <Route path="/register/*" element={<Register />} />
        </Routes>
        <Footer />
        <Outlet />
      </div>
    </BrowserRouter>
  );
}
