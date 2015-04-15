var petTrackerControllers = angular.module('petTrackerControllers', []);

petTrackerControllers.controller('PetTrackerController', [
    '$scope',
    'PetTrackerFactory',
    function($scope, PetTrackerFactory){
        console.log('working');
    }
]);
