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
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, './src/djangocms_leaflet/static/webpack'),
        clean: true,
    },
    // optimization: {
    //     minimize: false
    // },
    // mode: 'development',
    mode: 'production',
};
