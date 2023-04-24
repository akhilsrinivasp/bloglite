## Directory structure

```
frontend/
├── public
│   ├── favicon.ico
│   └── index.html
├── src
│   ├── App.vue
│   ├── assets
│   │   ├── fonts
│   │   │   └── *.ttf
│   │   ├── scss
│   │   │   └── styles.scss
│   ├── components
│   │   ├── BlogPost.vue
│   │   ├── EditBlog.vue
│   │   ├── EditUser.vue
│   │   ├── LoginComp.vue
│   │   ├── LogoutComp.vue
│   │   └── SignupComp.vue
│   ├── views
│   │   ├── BlogView.vue
│   │   ├── FeedView.vue
│   │   ├── HomeView.vue
│   │   ├── LoginView.vue
│   │   ├── SignupView.vue
│   │   ├── UploadBlog.vue
│   │   
│   ├── main.js
│   ├── router
│   │   └── router.js
│   └── store
│       └── store.js
├── babel.config.js
├── package-lock.json
├── package.json
└── vue.config.js
```
## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
