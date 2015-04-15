var petTrackerApp = angular.module('petTrackerApp', [
    'ngResource',
    'petTrackerControllers',
    'petTrackerDirectives',
    'petTrackerServices'
]);

petTrackerApp.config([
    '$interpolateProvider',
    '$resourceProvider',
    function($interpolateProvider, $resourceProvider){
        $interpolateProvider.startSymbol('[[').endSymbol(']]');
        $resourceProvider.defaults.stripTrailingSlashes = false;
    }
]);
