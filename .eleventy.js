module.exports = function (eleventyConfig) {
  eleventyConfig.addCollection("practices", (collectionApi) =>
    collectionApi
      .getFilteredByGlob("./src/practices/*.md")
      .filter((item) => !item.inputPath.endsWith("/practices/index.md"))
  );

  eleventyConfig.addCollection("framework", (collectionApi) =>
    collectionApi
      .getFilteredByGlob("./src/framework/*.md")
      .filter((item) => !item.inputPath.endsWith("/framework/index.md"))
  );

  eleventyConfig.addCollection("workshop", (collectionApi) =>
    collectionApi.getFilteredByGlob("./src/workshop/*.md")
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
