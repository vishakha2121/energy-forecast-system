import React from 'react';

function App() {
  return (
    <div style={{ 
      minHeight: '100vh', 
      display: 'flex', 
      alignItems: 'center', 
      justifyContent: 'center',
      flexDirection: 'column',
      fontFamily: 'Arial, sans-serif'
    }}>
      <h1 style={{ color: '#3b82f6' }}>⚡ Energy Forecast System</h1>
      <p>Frontend is running successfully!</p>
      <p>Backend API: <code>http://localhost:8000</code></p>
      <div style={{ marginTop: '20px' }}>
        <button onClick={() => fetch('http://localhost:8000/') 
          .then(res => res.json())
          .then(data => alert(JSON.stringify(data)))
          .catch(err => alert('Backend not running: ' + err))}
          style={{ padding: '10px 20px', background: '#3b82f6', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}>
          Test Backend Connection
        </button>
      </div>
    </div>
  );
}

export default App;