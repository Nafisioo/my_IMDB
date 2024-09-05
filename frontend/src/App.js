import axios from 'axios';
import React, { useState, useEffect } from 'react';    
import Movie from './Movie';  

function App() {  
  const [movieData, setMovieData] = useState(null);  

  const fetchMovieData = async (movieTitle) => {  
    try {  
      const response = await axios.get(`https://api.themoviedb.org/3/search/movie?api_key=bbc90b31f72ee820ce3088f7ab4d9a4f&query=${movieTitle}`);  
      return response.data;  
    } catch (error) {  
      console.error('Error fetching movie data:', error);  
      // Handle error
    }  
  };  

  useEffect(() => {  
    fetchMovieData('fight club'); // Fetch data on component mount  
  }, []);  

  return (  
    <div className="App">  
      {movieData && movieData.results.length > 0 && (  
        <Movie movie={movieData.results[0]} /> // Display the first result  
      )}  
    </div>  
  );  
}  

export default App;