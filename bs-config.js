module.exports = {
    proxy: "localhost:5001",
    files: [
        "templates/**/*.html",
        "static/css/*.css",
        "static/js/*.js"
    ],
    open: true,
    notify: false,
    reloadDelay: 500
}; 