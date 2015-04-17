var petTrackerApp = angular.module('petTrackerApp', [
    'ngResource',
    'petTrackerControllers',
    'petTrackerDirectives',
    'petTrackerFilters',
    'petTrackerServices'
]);

petTrackerApp.config([
    '$httpProvider',
    '$interpolateProvider',
    '$resourceProvider',
    function($httpProvider, $interpolateProvider, $resourceProvider){
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.useApplyAsync(true);
        $interpolateProvider.startSymbol('[[').endSymbol(']]');
        $resourceProvider.defaults.stripTrailingSlashes = false;
    }
]);
