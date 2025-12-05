module.exports = function (eleventyConfig) {
  eleventyConfig.addCollection("practices", (collectionApi) =>
    collectionApi.getFilteredByGlob("./practices/*.md")
  );

  eleventyConfig.addCollection("framework", (collectionApi) =>
    collectionApi.getFilteredByGlob("./framework/*.md")
  );

  eleventyConfig.addCollection("workshop", (collectionApi) =>
    collectionApi.getFilteredByGlob("./workshop/*.md")
  );

  eleventyConfig.addPassthroughCopy({ "src/favicon": "favicon" });
  eleventyConfig.addPassthroughCopy("src/styles.css");

  return {
    dir: {
      input: "src",
      includes: "_includes",
      data: "_data",
      output: "_site",
    },
  };
};
