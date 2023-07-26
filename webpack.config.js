const path = require('path');

module.exports = {
    entry: {
        'leaflet': './assets/src/leaflet.js',
    },
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ["style-loader", "css-loader"],
            },
        ],
    },
    output: {
        path: path.resolve(__dirname, './src/djangocms_leaflet/static/webpack'),
        filename: '[name].bundle.js',
        clean: true,
    },
    mode: 'production',
};
