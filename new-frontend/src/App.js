import React from 'react';
import './App.css';
import Header from './Header';
import Footer from './Footer';

function App() {
  return (
    <div className="App">
      <div className="content-wrap">
        <Header />
        <main>
          <p>Main Content</p>
        </main>
      </div>
      <Footer />
    </div>
  );
}

export default App;
