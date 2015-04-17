var petTrackerFilters = angular.module('petTrackerFilters', [])

petTrackerFilters.filter('slugify', function() {
  return function(input) {
        return input.toLowerCase()
                    .replace(/ |_/g,'-')
                    .replace(/[^\w-]+/g,'')
                    .replace(/[-]+/g, '-');
  }
})
