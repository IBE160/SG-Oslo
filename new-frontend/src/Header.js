import React from 'react';
import './Header.css';
import NavigationBar from './NavigationBar';

const Header = () => {
  return (
    <header className="app-header">
      <h1>StudyBuddy-AI</h1>
      <NavigationBar />
    </header>
  );
};

export default Header;
