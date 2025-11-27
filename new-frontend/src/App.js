import React from 'react';
import './App.css';
import Header from './Header';
import Footer from './Footer';
import DocumentUpload from './DocumentUpload';

function App() {
  return (
    <div className="App">
      <div className="content-wrap">
        <Header />
        <main>
          <DocumentUpload />
        </main>
      </div>
      <Footer />
    </div>
  );
}

export default App;
