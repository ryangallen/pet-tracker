var petTrackerServices = angular.module('petTrackerServices', ['ngResource'])

petTrackerServices.factory('PetTrackerFactory', [
    '$http',
    function($http){
        var endpoints = {
            animals: "/api/animals/",
            breeds: "/api/breeds/",
            pets: "/api/pets/",
        }

        return {
            readAnimals: function(){
                return $http.get(endpoints.animals);
            },
            readBreeds: function(){
                return $http.get(endpoints.breeds);
            },
            readPets: function(){
                return $http.get(endpoints.pets);
            },
            createPet: function(values){
                return $http.post(endpoints.pets, values);
            },
            deletePet: function(id){
                return $http.delete(endpoints.pets + id);
            },
        }
    }
]);
