#include <iostream>
#include <fstream>
#include <cstring>

struct Service {
    char serviceType[30]; 
    char serviceName[50];
    char serviceAddress[100];
    int serviceZip;
    float cost;
};


void addService() {
    Service service;
    std::ofstream outFile("services.dat", std::ios::binary | std::ios::app);

    std::cout << "Enter service type (e.g., plumber, electrician): ";
    std::cin.ignore();
    std::cin.getline(service.serviceType, 30);

    std::cout << "Enter service name: ";
    std::cin.getline(service.serviceName, 50);

    std::cout << "Enter address: ";
    std::cin.getline(service.serviceAddress, 100);

    std::cout << "Enter ZIP code: ";
    std::cin >> service.serviceZip;

    std::cout << "Enter cost: ";
    std::cin >> service.cost;

    outFile.write((char*)&service, sizeof(service));
    outFile.close();

    std::cout << "Service added successfully!\n";
}


void viewAllServices() {
    Service service;
    std::ifstream inFile("services.dat", std::ios::binary);

    if (!inFile) {
        std::cout << "Error: Could not open file!\n";
        return;
    }

    std::cout << "\nList of Services:\n";
    while (inFile.read((char*)&service, sizeof(service))) {
        std::cout << "Type: " << service.serviceType << "\n";
        std::cout << "Name: " << service.serviceName << "\n";
        std::cout << "Address: " << service.serviceAddress << "\n";
        std::cout << "ZIP Code: " << service.serviceZip << "\n";
        std::cout << "Cost: $" << service.cost << "\n\n";
    }
    inFile.close();
}


void searchService(const char* searchType) {
    Service service;
    std::ifstream inFile("services.dat", std::ios::binary);
    bool found = false;

    if (!inFile) {
        std::cout << "Error: Could not open file!\n";
        return;
    }

    std::cout << "\nSearching for services of type: " << searchType << "\n";
    while (inFile.read((char*)&service, sizeof(service))) {
        if (strcmp(service.serviceType, searchType) == 0) {  
            std::cout << "\nService Found:\n";
            std::cout << "Type: " << service.serviceType << "\n";
            std::cout << "Name: " << service.serviceName << "\n";
            std::cout << "Address: " << service.serviceAddress << "\n";
            std::cout << "ZIP Code: " << service.serviceZip << "\n";
            std::cout << "Cost: $" << service.cost << "\n\n";
            found = true;
        }
    }
    inFile.close();

    if (!found) {
        std::cout << "No services found for type '" << searchType << "'.\n";
    }
}
int main() {
    int choice;
    char searchType[50];

    do {
        std::cout << "1. Add Service\n2. View All Services\n3. Search Service\n4. Exit\nEnter choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                addService();
                break;
            case 2:
                viewAllServices();
                break;
            case 3:
                std::cout << "Enter the service name to search: ";
                std::cin.ignore();
                std::cin.getline(searchType, 50);
                searchService(searchType);
                break;
            case 4:
                std::cout << "Exiting program.\n";
                break;
            default:
                std::cout << "Invalid choice.\n";
        }
    } while (choice != 4);

    return 0;
}
