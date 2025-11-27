import React from 'react';
import './NavigationBar.css';

const NavigationBar = () => {
  return (
    <nav className="navigation-bar">
      <a href="#" className="nav-link active">Home</a>
      <a href="#" className="nav-link">Dashboard</a>
      <a href="#" className="nav-link">My Documents</a>
      <a href="#" className="nav-link">Settings</a>
    </nav>
  );
};

export default NavigationBar;
