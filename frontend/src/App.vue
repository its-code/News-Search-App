<template>
  <div id="app">
      <div class="search-container">
        <input v-model="query" class="search-input" placeholder="Search for news...">
        <select v-model="language" class="language-select">
          <option value="en">English</option>
          <option value="de">German</option>
        </select>
        <button @click="search" class="search-button">Search</button>
      </div>

      <!-- Loading spinner -->
      <div v-if="loading" class="loading">
        Loading...
      </div>
    
      <!-- Display message when no results are found -->
      <div v-if="results.length === 0 && searchInitiated && !loading" class="no-results">
        No results found for your search.
      </div>

      <!-- News Result Container -->
      <div class="results-container" v-for="result in results" :key="result.url">
        <img v-if="result.thumbnail" class="thumbnail" :src="result.thumbnail" alt="Thumbnail">
        <a class="news-title" :href="result.url">{{ result.title }}</a>
      </div>
  </div>
</template>


<!-- Fetching the results from Flask Back-End -->
<script>
export default {
  data() {
    return {
      query: "",
      language: "en",
      results: [],
      searchInitiated: false,
      loading: false
    };
  },
  methods: {
    async search() {
      this.searchInitiated = true;
      this.loading = true;

      const response = await fetch('http://localhost:5000/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: this.query, language: this.language })
      });

      this.results = await response.json();
      this.loading = false;  
    }
  }
};
</script>


<!-- CSS Styles for Application, button, news result, no results and loading -->

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 60px;
  width: 80%;
  margin-left: auto;
  margin-right: auto;
}

.results-container {
  display: flex;
  align-items: center;
  margin-top: 20px;
  border-bottom: 1px solid #e0e0e0;
  padding-bottom: 20px;
}

.thumbnail {
  width: 100px;
  height: 100px;
  object-fit: cover;
  margin-right: 20px;
  border-radius: 8px;
  box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.1);
}

.news-title {
  font-size: 18px;
  color: #333;
  text-decoration: none;
}

.news-title:hover {
  text-decoration: underline;
}

.search-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  margin-bottom: 40px;
}

.search-input {
  width: 300px;
  padding: 10px;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  outline: none;
  transition: border-color 0.3s;

  &:focus {
    border-color: #007BFF;
  }
}

.language-select {
  padding: 10px;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  outline: none;
  background-color: #f9f9f9;
  transition: border-color 0.3s;

  &:focus {
    border-color: #007BFF;
  }
}

.search-button {
  padding: 10px 20px;
  background-color: #007BFF;
  color: #ffffff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;

  &:hover {
    background-color: #0056b3;
  }
}

.no-results {
  margin-top: 40px;
  font-size: 18px;
  color: #666;
  text-align: center;
}

.loading {
  margin-top: 40px;
  font-size: 20px;
  color: #007BFF;
  text-align: center;
  font-weight: bold;
}

</style>
