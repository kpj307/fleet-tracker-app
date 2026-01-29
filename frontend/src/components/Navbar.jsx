import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import styles from "../styles/Navbar.module.css";

export default function Navbar() {
  const navigate = useNavigate();
  const [open, setOpen] = useState(false);

  const logout = () => {
    localStorage.clear();
    navigate("/login");
  };

  return (
    <nav className={styles.navbar}>
  
      <div className={styles.brand}>🚗 Fleet Tracker</div>
      {/* Hamburger */}
      <button
        className={styles.menuBtn}
        onClick={() => setOpen(!open)}
      >
        ☰
      </button>

      <div className={`${styles.links} ${open ? styles.show : ""}`}>
        <Link onClick={() => setOpen(false)} to="/">Dashboard</Link>
        <Link onClick={() => setOpen(false)} to="/">Vehicles</Link>
        <button onClick={logout} className={styles.logout}>
          Logout
        </button>
      </div>
    </nav>
  );
}
