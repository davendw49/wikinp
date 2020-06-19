devServer: {
	  clientLogLevel: 'warning',
		  historyApiFallback: true,
		  hot: true,
		  compress: true,
		  host: HOST || config.dev.host,
		  port: PORT || config.dev.port,
		  open: config.dev.autoOpenBrowser,
		  overlay: config.dev.errorOverlay
	   ? { warnings: false, errors: true }
	   : false,
		  publicPath: config.dev.assetsPublicPath,
		  proxy: config.dev.proxyTable,
		  quiet: true, // necessary for FriendlyErrorsPlugin
		  disableHostCheck: true,
		  watchOptions: {
			     poll: config.dev.poll,
				    }
	 }
