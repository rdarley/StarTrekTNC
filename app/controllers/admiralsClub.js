app.controller('AdmiralsClub', function ($http) {
	var vm = this;

	$http({
		method: 'GET',
		url: 'https://itunes.apple.com/us/rss/customerreviews/id=1193095604/sortBy=mostRecent/json'
	}).then(function (response) {
		
		// setup reviews array from response
		vm.reviews = response.data.feed.entry;
		
		// Remove weird first entry that isn't a review...
		vm.reviews.shift();
		
		// initialize empty array to push 5 star reviews into
		vm.admiralsClub = [];
		
		// add star ratings and only grab the 5 star reviews
		for (var i = 0; i < vm.reviews.length; i++) {
			if (vm.reviews[i]['im:rating'].label === '5') {
				vm.reviews[i].rating = '<i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>';
				
				vm.admiralsClub.push(vm.reviews[i]);
			}
		}
	}, function (response) {
		// the call failed
		console.log('That did not work');
	});
});