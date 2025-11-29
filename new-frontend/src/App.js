import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import Header from './Header';
import Footer from './Footer';
import MainPage from './MainPage';
import DocumentViewer from './DocumentViewer';

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <div className="content-wrap">
          <Header />
          <main>
            <Routes>
              <Route path="/" element={<MainPage />} />
              <Route path="/document/:documentId" element={<DocumentViewer />} />
            </Routes>
          </main>
        </div>
        <Footer />
      </div>
    </BrowserRouter>
  );
}

export default App;
