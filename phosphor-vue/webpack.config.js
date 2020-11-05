const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
  mode: 'development',
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: `${__dirname}/`,
  },
  module: {
    rules: [
      { test: /\.vue$/, loader: 'vue-loader', },
      //{ test: /\.js$/, loader: 'babel-loader', },
      { test: /\.css$/, use: [ 'vue-style-loader', 'css-loader', ], },
    ]
  },
  plugins: [
    new VueLoaderPlugin(),
  ],
  resolve: {
    extensions: ['.vue', '.js'],
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    }
  },
}