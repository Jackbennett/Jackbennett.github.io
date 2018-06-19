var Metalsmith = require('metalsmith');
var layouts = require('metalsmith-layouts');
var inPlace = require('metalsmith-in-place');
var autoprefixer = require('metalsmith-autoprefixer');
var assets = require('metalsmith-assets');
var markdown = require('metalsmith-markdown');
var drafts = require('metalsmith-drafts');
var permalinks = require('metalsmith-permalinks');
var collections = require('metalsmith-collections');
var debug = require('metalsmith-debug');

Metalsmith(__dirname)
  .destination('./public')
  .source('./content')
  .clean(true)
  .use(assets({
    source: './assets',
    destination: './assets'
  }))
  .use(drafts())
  .use(collections({
      blog:{
        pattern:'blog/**/*.html',
        sortBy: 'date',
        reverse: true
      }
  }))
  .use(permalinks({
    pattern: ':title',
    relative: false,
    linksets: [{
        match: { collection: 'blog' },
        pattern: ':collection/:title'
    }]
  }))
  .use(autoprefixer())
  .use(inPlace({pattern: '**/*.hbs'}))
  .use(layouts({
    engine: 'handlebars',
    directory: './template',
    default: 'default.hbs',
    partials: './template/partial',
    pattern: '**/*.html'
  }))
  .use(debug())  // set $env:DEBUG='metalsmith:*' to see output
  .build(function(err) {
    if (err) throw err;
  })
