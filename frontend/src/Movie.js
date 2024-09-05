import React from 'react';  

const Movie = ({ movie }) => {  
    const posterUrl = `https://image.tmdb.org/t/p/w500${movie.poster_path}`; // Construct poster URL  
    return (  
      <div className="movie">  
        {movie.poster_path && <img src={posterUrl} alt={movie.title} />}  
        <h2>{movie.title}</h2>  
        <p>Release Date: {movie.release_date}</p>  
        <p>Overview: {movie.overview}</p>  
        {/* Add other movie details as needed */}  
      </div>  
    );  
  };  

export default Movie;