var petTrackerControllers = angular.module('petTrackerControllers', []);

petTrackerControllers.controller('PetTrackerController', [
    '$scope',
    'PetTrackerFactory',
    function($scope, PetTrackerFactory){
        PetTrackerFactory.readAnimals().then(
            function(promise){
                $scope.animals = promise.data.results;
            }
        );
        PetTrackerFactory.readBreeds().then(
            function(promise){
                $scope.breeds = promise.data.results;
            }
        );
        PetTrackerFactory.readPets().then(
            function(promise){
                $scope.pets = promise.data.results;
            }
        );
    }
]);
