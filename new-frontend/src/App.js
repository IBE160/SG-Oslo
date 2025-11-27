import React from 'react';
import './App.css';
import Header from './Header';
import Footer from './Footer';
import DocumentUpload from './DocumentUpload';
import DocumentList from './DocumentList';

function App() {
  return (
    <div className="App">
      <div className="content-wrap">
        <Header />
        <main>
          <DocumentUpload />
          <DocumentList />
        </main>
      </div>
      <Footer />
    </div>
  );
}

export default App;
