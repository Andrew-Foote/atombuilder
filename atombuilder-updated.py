# atombuilder.py
# Need to work on the electrons, they don't work

from __future__ import division
import pygame, sys, random
from pygame.locals import *
pygame.init()

class Atom:
    ELEMENTS = [
        'Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen',
        'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminium', 'Silicon',
        'Phosphorus', 'Sulphur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium',
        'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel',
        'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine',
        'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum',
        'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium',
        'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Caesium', 'Barium', 'Lanthanum',
        'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium',
        'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium',
        'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium',
        'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium',
        'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium',
        'Uranium', 'Neptuninium', 'Plutonium', 'Americium', 'Curium', 'Berkelium',
        'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium',
        'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium',
        'Darmstadtium', 'Roentgenium', 'Ununbium', 'Ununtrium', 'Ununquadium',
        'Ununpentium', 'Ununhexium', 'Ununseptium', 'Ununoctium'
    ]
    SHELL_FILLING_ORDER = [
            1,                                                                                           1,
            2, 2,                                                                         2, 2, 2, 2, 2, 2,
            3, 3,                                                                         3, 3, 3, 3, 3, 3,
            4, 4,                                           3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4,
            5, 5,                                           4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5,
            6, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6,
            7, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7
    ]
    STABLE_ISOTOPES = [
        'Nothing', 'Electron', 'Proton', 'Deuteron', 'Impossible', 'Hydrogen', 'Deuterium',
        'Helium-3', 'Helium-4', 'Lithium-6', 'Lithium-7', 'Beryllium-9', 'Boron-10',
        'Boron-11', 'Carbon-12', 'Carbon-13', 'Nitrogen-14', 'Nitrogen-15', 'Oxygen-16',
        'Oxygen-17', 'Oxygen-18', 'Fluorine-19', 'Neon-20', 'Neon-21', 'Neon-22',
        'Sodium-23', 'Magnesium-24', 'Magnesium-25', 'Magnesium-26', 'Hydrogen-2',
        'Aluminium-27', 'Silicon-28', 'Silicon-29', 'Silicon-30', 'Phosphorus-31', 'Sulphur-32',
        'Sulphur-33', 'Sulphur-34', 'Sulphur-36', 'Chlorine-35', 'Chlorine-37', 'Argon-36',
        'Argon-38', 'Argon-40', 'Potassium-39', 'Potassium-41', 'Calcium-40', 'Calcium-42',
        'Calcium-43', 'Calcium-44', 'Calcium-46', 'Scandium-45', 'Titanium-46',
        'Titanium-47', 'Titanium-48', 'Titanium-49', 'Titanium-50', 'Vanadium-51',
        'Chromium-50', 'Chromium-52', 'Chromium-53', 'Chromium-54', 'Manganese-55', 'Iron-54', 'Iron-56',
        'Iron-57', 'Iron-58', 'Cobalt-59', 'Nickel-58', 'Nickel-60', 'Nickel-61', 'Nickel-62',
        'Nickel-64', 'Copper-63', 'Copper-65', 'Zinc-64', 'Zinc-66', 'Zinc-67', 'Zinc-68',
        'Zinc-70', 'Gallium-69', 'Gallium-71', 'Germanium-70', 'Germanium-72', 'Germanium-73',
        'Germanium-74', 'Arsenic-75', 'Selenium-74', 'Selenium-76', 'Selenium-77',
        'Selenium-78', 'Selenium-80', 'Bromine-79', 'Bromine-81', 'Krypton-80', 'Krypton-82',
        'Krypton-83', 'Krypton-84', 'Krypton-86', 'Rubidium-85', 'Strontium-84', 'Strontium-86',
        'Strontium-87', 'Strontium-88', 'Yttrium-89', 'Zirconium-90', 'Zirconium-91',
        'Zirconium-92', 'Zirconium-94', 'Niobium-93', 'Molybdenum-92', 'Molybdenum-94',
        'Molybdenum-95', 'Molybdenum-96', 'Molybdenum-97', 'Molybdenum-98', 'Ruthenium-96',
        'Ruthenium-98', 'Ruthenium-99', 'Ruthenium-100', 'Ruthenium-101', 'Ruthenium-102',
        'Ruthenium-104', 'Palladium-102', 'Palladium-104', 'Palladium-105', 'Palladium-106',
        'Palladium-108', 'Palladium-110', 'Silver-107', 'Silver-109', 'Cadmium-106',
        'Cadmium-108', 'Cadmium-110', 'Cadmium-111', 'Cadmium-112', 'Cadmium-114', 'Indium-113',
        'Tin-112', 'Tin-114', 'Tin-115', 'Tin-116', 'Tin-117', 'Tin-118', 'Tin-119', 'Tin-120',
        'Tin-122', 'Tin-124', 'Antimony-121', 'Antimony-123', 'Tellurium-120', 'Tellurium-122',
        'Tellurium-123', 'Tellurium-124', 'Tellurium-125', 'Tellurium-126', 'Iodine-127',
        'Xenon-124', 'Xenon-126', 'Xenon-128', 'Xenon-129', 'Xenon-130', 'Xenon-131',
        'Xenon-132', 'Xenon-134', 'Xenon-136', 'Caesium-133', 'Barium-132', 'Barium-134',
        'Barium-135', 'Barium-136', 'Barium-137', 'Barium-138', 'Lanthanum-139', 'Cerium-136',
        'Cerium-138', 'Cerium-140', 'Cerium-142', 'Praseodymium-141', 'Neodymium-142',
        'Neodymium-143', 'Neodymium-145', 'Neodymium-146', 'Neodymium-148', 'Samarium-144',
        'Samarium-149', 'Samarium-150', 'Samarium-152', 'Samarium-154', 'Europium-153',
        'Gadolinium-154', 'Gadolinium-155', 'Gadolinium-156', 'Gadolinium-157', 'Gadolinium-158',
        'Gadolinium-160', 'Dysprosium-156', 'Dysprosium-158', 'Dysprosium-160', 'Dysprosium-161',
        'Dysprosium-161', 'Dysprosium-162', 'Dysprosium-163', 'Dysprosium-164', 'Holmium-165',
        'Erbium-162', 'Erbium-164', 'Erbium-166', 'Erbium-167', 'Erbium-168', 'Erbium-170',
        'Thulium-169', 'Ytterbium-168', 'Ytterbium-170', 'Ytterbium-171', 'Ytterbium-172',
        'Ytterbium-173', 'Ytterbium-174', 'Ytterbium-176', 'Lutetium-175', 'Tantalum-181',
        'Tungsten-182', 'Tungsten-183', 'Tungsten-184', 'Tungsten-186', 'Rhenium-185',
        'Osmium-184', 'Osmium-187', 'Osmium-188', 'Osmium-189', 'Osmium-190', 'Osmium-192',
        'Iridium-191', 'Iridium-193', 'Platinum-192', 'Platinum-194', 'Platinum-195',
        'Platinum-196', 'Platinum-198', 'Gold-197', 'Mercury-196', 'Mercury-198', 'Mercury-199',
        'Mercury-200', 'Mercury-201', 'Mercury-202', 'Mercury-204', 'Thallium-203',
        'Thallium-205', 'Lead-204', 'Lead-206', 'Lead-207', 'Lead-208'
    ]
    THOUSAND_ISOTOPES = [
        'Neutronium', 'Calcium-47', 'Scandium-44', 'Scandium-47', 'Scandium-48', 'Manganese-52',
        'Cobalt-60', 'Nickel-56', 'Nickel-57', 'Nickel-66', 'Copper-67', 'Zinc-72',
        'Gallium-67', 'Germanium-69', 'Arsenic-71', 'Arsenic-72', 'Arsenic-76', 'Arsenic-77',
        'Selenium-72', 'Bromine-77', 'Bromine-82', 'Krypton-79', 'Strontium-83', 'Yttrium-87',
        'Yttrium-90', 'Zirconium-89', 'Molybdenum-99', 'Technetium-96', 'Ruthenium-97',
        'Rhodium-105', 'Palladium-100', 'Silver-106', 'Silver-111', 'Indium-111', 'Tin-125',
        'Antimony-119', 'Antimony-120', 'Antimony-122', 'Antimony-127', 'Tellurium-118',
        'Tellurium-119', 'Tellurium-131', 'Tellurium-132', 'Iodine-124', 'Iodine-131',
        'Xenon-133', 'Caesium-129', 'Caesium-131', 'Caesium-132', 'Barium-128', 'Lanthanum-140',
        'Cerium-134', 'Cerium-137', 'Cerium-143', 'Neodymium-140', 'Prometheum-149',
        'Prometheum-151', 'Samarium-153', 'Gadolinium-147', 'Gadolinium-149', 'Terbium-153',
        'Terbium-155', 'Terbium-156', 'Terbium-161', 'Dysprosium-166', 'Erbium-160',
        'Erbium-169', 'Erbium-172', 'Thulium-165', 'Thulium-167', 'Thulium-172', 'Ytterbium-166',
        'Ytterbium-175', 'Lutetium-169', 'Lutetium-170', 'Lutetium-171', 'Lutetium-172',
        'Hafnium-176', 'Hafnium-177', 'Hafnium-178', 'Hafnium-179', 'Hafnium-180',
        'Tantalum-177', 'Tantalum-183', 'Rhenium-182', 'Rhenium-189', 'Osmium-193',
        'Iridium-188', 'Platinum-191', 'Gold-194', 'Gold-196', 'Gold-198', 'Gold-199',
        'Mercury-195', 'Mercury-197', 'Thallium-200', 'Thallium-201', 'Lead-203', 'Bismuth-206',
        'Bismuth-210', 'Polonium-206', 'Radon-222', 'Radium-224', 'Actinium-225',
        'Actinium-226', 'Thorium-231', 'Protactinium-229', 'Protactinium-232', 'Uranium-231',
        'Uranium-237', 'Neptuninium-234', 'Neptuninium-238', 'Neptuninium-239',
        'Plutonium-247', 'Americium-240', 'Berkelium-245', 'Berkelium-246', 'Californium-246',
        'Einsteinium-251', 'Fermium-252', 'Fermium-253', 'Dubnium-268'
    ]
    TEN_THOUSAND_ISOTOPES = [
        'Beryllium-7', 'Phosphorus-32', 'Phosphorus-33', 'Sulphur-35', 'Argon-37',
        'Scandium-46', 'Vanadium-48', 'Chromium-51', 'Iron-59', 'Cobalt-56', 'Cobalt-58',
        'Germanium-71', 'Arsenic-73', 'Arsenic-74', 'Selenium-75', 'Rubidium-83', 'Rubidium-84',
        'Rubidium-86', 'Strontium-82', 'Strontium-85', 'Strontium-89', 'Yttrium-91',
        'Zirconium-88', 'Zirconium-95', 'Niobium-95', 'Technetium-95', 'Ruthenium-103',
        'Rhodium-99', 'Rhodium-102', 'Palladium-103', 'Cadmium-115', 'Indium-114',
        'Antimony-124', 'Antimony-126', 'Tellurium-129', 'Iodine-125', 'Iodine-126',
        'Xenon-127', 'Caesium-136', 'Barium-131', 'Barium-140', 'Cerium-141', 'Praseodymium-143',
        'Neodymium-147', 'Prometheum-148', 'Europium-147', 'Europium-148', 'Europium-149',
        'Europium-156', 'Gadolinium-146', 'Terbium-160', 'Thulium-168', 'Ytterbium-169',
        'Hafnium-175', 'Tungsten-178', 'Tungsten-185', 'Tungsten-188', 'Rhenium-183',
        'Osmium-185', 'Iridium-189', 'Iridium-190', 'Platinum-188', 'Mercury-203',
        'Thallium-202', 'Bismuth-205', 'Radium-223', 'Radium-225', 'Thorium-227', 'Thorium-234',
        'Protactinium-230', 'Protactinium-233', 'Uranium-230', 'Plutonium-237',
        'Plutonium-246', 'Curium-240', 'Curium-241', 'Californium-253', 'Californium-254',
        'Einsteinium-253', 'Einsteinium-255', 'Mendelevium-258', 'Mendelevium-260'
    ]
    HUNDRED_THOUSAND_ISOTOPES = [
        'Sodium-22', 'Calcium-45', 'Vanadium-49', 'Manganese-54', 'Iron-55', 'Cobalt-57',
        'Zinc-65', 'Germanium-68', 'Yttrium-88', 'Ruthenium-106', 'Rhodium-101', 'Silver-110',
        'Cadmium-109', 'Tin-113', 'Tin-123', 'Antimony-125', 'Tellurium-121', 'Tellurium-127',
        'Caesium-134', 'Cerium-139', 'Cerium-144', 'Prometheum-143', 'Prometheum-144',
        'Prometheum-146', 'Prometheum-147', 'Samarium-145', 'Europium-154', 'Europium-155',
        'Gadolinium-151', 'Gadolinium-153', 'Dysprosium-159', 'Thulium-170', 'Thulium-171',
        'Lutetium-173', 'Lutetium-174', 'Lutetium-177', 'Hafnium-172', 'Hafnium-181',
        'Tantalum-179', 'Tantalum-182', 'Tungsten-181', 'Rhenium-184', 'Osmium-194',
        'Gold-195', 'Thallium-205', 'Polonium-208', 'Polonium-210', 'Radium-228', 'Thorium-228',
        'Neptuninium-235', 'Plutonium-236', 'Curium-242', 'Berkelium-248', 'Berkelium-249',
        'Californium-248', 'Californium-252', 'Einsteinium-252', 'Einsteinium-254',
        'Fermium-257'
    ]
    MILLION_ISOTOPES = [
        'Hydrogen-3', 'Tritium', 'Carbon-14', 'Silicon-32', 'Argon-39', 'Argon-42', 'Titanium-44',
        'Nickel-63', 'Krypton-85', 'Strontium-90', 'Niobium-91', 'Molybdenum-93', 'Silver-108',
        'Tin-121', 'Caesium-137', 'Barium-133', 'Prometheum-145', 'Samarium-151',
        'Europium-150', 'Europium-152', 'Gadolinium-148', 'Terbium-157', 'Terbium-158',
        'Holmium-163', 'Holmium-166', 'Iridium-192', 'Platinum-193', 'Mercury-194',
        'Lead-210', 'Bismuth-207', 'Polonium-209', 'Radium-226', 'Actinium-227', 'Thorium-229',
        'Uranium-232', 'Plutonium-238', 'Plutonium-240', 'Plutonium-241', 'Americium-241',
        'Americium-242', 'Americium-243', 'Curium-243', 'Curium-244', 'Curium-245',
        'Curium-246', 'Curium-250', 'Berkelium-247', 'Californium-249', 'Californium-250',
        'Californium-251'
    ]
    TEN_MILLION_ISOTOPES = [
        'Beryllium-10', 'Aluminium-26', 'Chlorine-36', 'Calcium-41', 'Vanadium-50'
        'Manganese-53', 'Iron-60', 'Nickel-59', 'Selenium-79', 'Krypton-81', 'Zirconium-93',
        'Niobium-92', 'Niobium-94', 'Technetium-97', 'Technetium-98', 'Technetium-99',
        'Palladium-107', 'Tin-126', 'Iodine-129', 'Caesium-135', 'Lanthanum-137',
        'Samarium-146', 'Gadolinium-150', 'Dysprosium-154', 'Hafnium-182', 'Rhenium-186',
        'Lead-202', 'Lead-205', 'Bismuth-208', 'Thorium-230', 'Protactinium-231', 'Uranium-233',
        'Uranium-234', 'Uranium-236', 'Neptuninium-236', 'Neptuninium-237', 'Plutonium-239',
        'Plutonium-242', 'Plutonium-244', 'Curium-247', 'Curium-248'
    ]
    HUNDRED_MILLION_ISOTOPES = [
        'Potassium-40', 'Calcium-48', 'Germanium-76', 'Selenium-82', 'Krypton-78', 'Rubidium-87',
        'Zirconium-96', 'Molybdenum-100', 'Cadmium-113', 'Cadmium-116', 'Indium-115',
        'Tellurium-128', 'Tellurium-130', 'Barium-130', 'Lanthanum-138', 'Neodymium-144',
        'Neodymium-150', 'Samarium-147', 'Samarium-148', 'Europium-151', 'Gadolinium-152',
        'Lutetium-176', 'Hafnium-174', 'Tantalum-180', 'Rhenium-187', 'Osmium-186',
        'Platinum-190', 'Bismuth-209', 'Thorium-232', 'Uranium-235', 'Uranium-238'
    ]
    def __init__(self, master, protons, neutrons, electrons):
        self.master = master
        self.atomic_number = self.protons = protons
        self.neutrons = neutrons
        self.electrons = electrons
        self.atomic_mass = self.isotope = self.protons + self.neutrons
        self.charge = self.protons - self.electrons
        self.shells = [ # in the opposite order so they don't cover each other up
            ElectronShell(self, 7), ElectronShell(self, 6), ElectronShell(self, 5),
            ElectronShell(self, 4), ElectronShell(self, 3), ElectronShell(self, 2),
            ElectronShell(self, 1)
        ]
        self.shells.reverse()
        # get the element name
        if self.protons == 0 and self.neutrons == 0 and self.electrons == 0:
            self.element = "Nothing"
        elif self.protons == 0 and self.neutrons == 1 and self.electrons == 0:
            self.element = "Neutron"
        elif self.protons == 0 and self.neutrons == 0 and self.electrons > 0:
            self.element = "Electron"
        elif self.protons == 0 and self.electrons == 0 and self.neutrons > 1:
            self.element = "Neutronium"
        elif self.protons == 0 and self.electrons > 0 and self.neutrons > 0:
            self.element = "Impossible"
        elif self.protons == 2 and self.neutrons == 0:
            self.element = "Impossible"
        elif self.protons == 1 and self.neutrons == 0 and self.electrons == 0:
            self.element = "Proton"
        elif self.protons == 1 and self.electrons == 1 and self.neutrons == 0:
            self.element = "Hydrogen"
        elif self.protons == 1 and self.neutrons == 1:
            self.element = "Deuterium"
        elif self.protons == 1 and self.neutrons == 2:
            self.element = "Tritium"
        else:
            try:
                self.element = Atom.ELEMENTS[self.atomic_number - 1] + '-' + str(self.isotope)
            except IndexError:
                self.element = "Unknown"
        
        # determine radioactivity
        if self.element in Atom.STABLE_ISOTOPES:
            self.radioactivity = None
        elif self.element in Atom.THOUSAND_ISOTOPES:
            self.radioactivity = 10000
        elif self.element in Atom.TEN_THOUSAND_ISOTOPES:
            self.radioactivity = 100000
        elif self.element in Atom.HUNDRED_THOUSAND_ISOTOPES:
            self.radioactivity = 1000000
        elif self.element in Atom.MILLION_ISOTOPES:
            self.radioactivity = 10000000
        elif self.element in Atom.TEN_MILLION_ISOTOPES:
            self.radioactivity = 100000000
        elif self.element in Atom.HUNDRED_MILLION_ISOTOPES:
            self.radioactivity = 1000000000
        else:
            self.radioactivity = 1000
        if self.radioactivity:
            print("Atom of", self.element, "made with radioactivity of", self.radioactivity)
        else:
            print("Stable atom of", self.element, "made")
    
    def try_decay(self):
        if self.radioactivity: # roll and decay if it reaches the upper limit
            decider = random.randrange(1, self.radioactivity + 1)
            if decider == self.radioactivity:
                return True

    def render(self):
        #### Render the nucleus
        # first we need to find a nice way to arrange the nucleus
        square = 0
        while square ** 2 < (self.protons + self.neutrons):
            square += 1 # find a square number big enough for the nucleons
        nucleus_size = square * 12
        nucleus = pygame.Surface((nucleus_size, nucleus_size))
        nucleus.convert()
        # now draw in the nucleons
        nucleus_append_area = (0, 0) # where the next particle should be blitted to
        protons_rendered = 0
        neutrons_rendered = 0
        while not (protons_rendered == self.protons and neutrons_rendered == self.neutrons):
            self.master.load_images()
            if protons_rendered < self.protons:
                proton = pygame.image.load('proton.bmp')
                proton.convert()
                nucleus.blit(proton, nucleus_append_area)
                if nucleus_append_area[0] + 12 < nucleus_size: # if it has not reached the edge
                    nucleus_append_area = (nucleus_append_area[0] + 12, nucleus_append_area[1])
                else: # move to the next row
                    nucleus_append_area = (0, nucleus_append_area[1] + 12)
                protons_rendered += 1
            if neutrons_rendered < self.neutrons:
                neutron = pygame.image.load('neutron.bmp')
                neutron.convert()
                nucleus.blit(neutron, nucleus_append_area)
                if nucleus_append_area[0] + 12 < nucleus_size: # if it has not reached the edge
                    nucleus_append_area = (nucleus_append_area[0] + 12, nucleus_append_area[1])
                else: # move to the next row
                    nucleus_append_area = (0, nucleus_append_area[1] + 12)
                neutrons_rendered += 1
        # Now we need to centre the nucleus in the atom area
        x = self.master.atom_area.get_rect().centerx - (nucleus_size / 2)
        y = self.master.atom_area.get_rect().centery - (nucleus_size / 2)
        self.master.atom_area.blit(nucleus, (x, y))
        
        ### Next job: draw the electrons
        electrons_rendered = 0
        for shell in Atom.SHELL_FILLING_ORDER:
            if electrons_rendered < self.electrons:
                self.master.load_images()
                self.shells[shell - 1].add_electron()
                electrons_rendered += 1
            else:
                break
        
        ### Final job: update the displayers
        self.master.displayer_bar.fill(Window.BACKGROUND_COLOUR)
        self.master.element_displayer = pygame.font.Font(None, Window.FONT_SIZE).render(self.element, 1, Window.DISPLAYER_COLOUR)
        self.master.atomic_number_displayer = pygame.font.Font(None, Window.FONT_SIZE).render(str(self.atomic_number), 1, Window.PROTON_COLOUR)
        self.master.atomic_mass_displayer = pygame.font.Font(None, Window.FONT_SIZE).render(str(self.atomic_mass), 1, Window.NEUTRON_COLOUR)
        self.master.charge_displayer = pygame.font.Font(None, Window.FONT_SIZE).render(str(self.charge), 1, Window.ELECTRON_COLOUR)
        if self.radioactivity == None:
            self.master.radioactivity_displayer = pygame.font.Font(None, Window.FONT_SIZE).render("Stable", 1, Window.ANTINEUTRINO_COLOUR)
        elif self.radioactivity == 10000:
            self.master.radioactivity_displayer = pygame.font.Font(None, Window.FONT_SIZE).render("Very unstable", 1, Window.ANTINEUTRINO_COLOUR)
        else:
            self.master.radioactivity_displayer = pygame.font.Font(None, Window.FONT_SIZE).render("Radioactive", 1, Window.ANTINEUTRINO_COLOUR)

class ElectronShell:
    SHELL_DIMENSIONS = [(280, 280), (300, 300), (320, 320), (340, 340), (360, 360), (380, 380), (400, 400)]
    SHELL_OFFSETS = [(85, 85), (75, 75), (65, 65), (55, 55), (45, 45), (35, 35), (25, 25)]
    SHELL_SIZES = [2, 8, 18, 32, 32, 18, 8]
    SHELL_COLOURS = [(70, 70, 70), (60, 60, 60), (50, 50, 50), (40, 40, 40), (30, 30, 30), (20, 20, 20), (10, 10, 10)]
    def __init__(self, master, number):
        self.master = master
        self.number = number
        self.area = pygame.Surface(ElectronShell.SHELL_DIMENSIONS[self.number - 1])
        self.area.convert()
        #self.area.fill(ElectronShell.SHELL_COLOURS[self.number - 1])
        self.size = ElectronShell.SHELL_SIZES[self.number - 1]
        self.rect = Rect(ElectronShell.SHELL_OFFSETS[self.number - 1], ElectronShell.SHELL_DIMENSIONS[self.number - 1])
        self.electrons = 0
        self.ELECTRON_POSITIONS = [
            self.rect.topleft, self.rect.bottomright, self.rect.topright, self.rect.bottomleft, # corners
            self.rect.midtop, self.rect.midleft, self.rect.midbottom, self.rect.midright, # middles
            (self.rect.centerx // 2, 0), (self.rect.centerx + self.rect.centerx // 2, 0), # quartiles on top
            (self.rect.centerx // 2, self.rect.bottom), (self.rect.centerx + self.rect.centerx // 2, 0), # quartiles on bottom
            (0, self.rect.centery // 2), (0, self.rect.centery + self.rect.centery // 2), # quartiles on the left
            (self.rect.right, self.rect.centery // 2), (self.rect.right, self.rect.centery + self.rect.centery // 2), # quartiles on the right
        ]
        self.master.master.atom_area.blit(self.area, ElectronShell.SHELL_OFFSETS[self.number - 1])
    def add_electron(self):
        electron = pygame.image.load('electron.bmp')
        electron.convert()
        self.master.master.atom_area.blit(electron, self.ELECTRON_POSITIONS[self.electrons])
        self.electrons += 1

class Window:
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500
    BACKGROUND_COLOUR = (0, 0, 0)
    PROTON_COLOUR = (0, 0, 255)
    NEUTRON_COLOUR = (255, 0, 0)
    ELECTRON_COLOUR = (0, 255, 0)
    ANTINEUTRINO_COLOUR = (0, 255, 255)
    PHOTON_COLOUR = (255, 255, 0)
    DISPLAYER_COLOUR = (255, 255, 255)
    FONT_SIZE = 25
    BORDER = 25
    def __init__(self):
        self.window = pygame.display.set_mode((Window.WINDOW_WIDTH, Window.WINDOW_HEIGHT))
        pygame.display.set_caption('Atom Builder')
        self.background = pygame.Surface((Window.WINDOW_WIDTH, Window.WINDOW_HEIGHT))
        self.background.convert()
        self.background.fill(Window.BACKGROUND_COLOUR)

        self.load_images()
        self.clock = pygame.time.Clock()
        self.do_radioactivity = True
        
        self.displayer_bar = pygame.Surface((Window.WINDOW_WIDTH, Window.BORDER)) 
        self.element_displayer = pygame.font.Font(None, Window.FONT_SIZE).render("Hydrogen", 1, (Window.DISPLAYER_COLOUR))
        self.atomic_number_displayer = pygame.font.Font(None, Window.FONT_SIZE).render("1", 1, (Window.PROTON_COLOUR))
        self.atomic_mass_displayer = pygame.font.Font(None, Window.FONT_SIZE).render("1", 1, (Window.NEUTRON_COLOUR))
        self.charge_displayer = pygame.font.Font(None, Window.FONT_SIZE).render("0", 1, (Window.ELECTRON_COLOUR))
        self.radioactivity_displayer = pygame.font.Font(None, Window.FONT_SIZE).render("Stable", 1, (Window.ANTINEUTRINO_COLOUR))
        self.displayer_bar.convert()
        
        self.button_bar = pygame.Surface((Window.BORDER, Window.WINDOW_HEIGHT))
        self.proton_button = pygame.image.load('proton.bmp')
        self.proton_button.convert()
        self.neutron_button = pygame.image.load('neutron.bmp')
        self.neutron_button.convert()
        self.electron_button = pygame.image.load('electron.bmp')
        self.electron_button.convert()
        self.button_bar.convert()
        
        self.atom_area = pygame.Surface((450, 450))
        self.atom_area.convert()
        self.atom = Atom(self, 0, 0, 0)
        
        self.reset_button = pygame.font.Font(None, Window.FONT_SIZE).render("Reset", 1, Window.DISPLAYER_COLOUR)
        self.reset_button.convert()
        
        self.update()
        
        while 1:
            self.handle_events()
        
    def update(self):
        self.clock.tick(10)
        self.atom.render()
        
        self.displayer_bar.blit(self.element_displayer, (0, 2))
        self.displayer_bar.blit(self.atomic_number_displayer, (200, 2))
        self.displayer_bar.blit(self.atomic_mass_displayer, (250, 2))
        self.displayer_bar.blit(self.charge_displayer, (300, 2))
        self.displayer_bar.blit(self.radioactivity_displayer, (350, 2))
        self.background.blit(self.displayer_bar, (Window.BORDER, 0))
        
        self.button_bar.blit(self.proton_button, (6, 0))
        self.button_bar.blit(self.neutron_button, (6, 20))
        self.button_bar.blit(self.electron_button, (6, 40))
        self.background.blit(self.button_bar, (0, Window.BORDER))
        
        self.background.blit(self.reset_button, (0, Window.WINDOW_HEIGHT - Window.FONT_SIZE))
        self.background.blit(self.atom_area, (Window.BORDER, Window.BORDER))
        self.window.blit(self.background, (0, 0))
        pygame.display.update()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.pos[0] > 6 and event.pos[0] < 18: # on the button bar
                    if event.pos[1] > Window.BORDER and event.pos[1] < Window.BORDER + 13:
                        print("Adding a proton.")
                        self.atom = Atom(self, self.atom.protons + 1, self.atom.neutrons, self.atom.electrons)
                        self.update()
                    elif event.pos[1] > Window.BORDER + 20 and event.pos[1] < Window.BORDER + 33:
                        print("Adding a neutron.")
                        self.atom = Atom(self, self.atom.protons, self.atom.neutrons + 1, self.atom.electrons)
                        self.update()
                    elif event.pos[1] > Window.BORDER + 40 and event.pos[1] < Window.BORDER + 53:
                        print("Adding an electron.")
                        self.atom = Atom(self, self.atom.protons, self.atom.neutrons, self.atom.electrons + 1)
                        self.update()
                elif event.pos[0] > 0 and event.pos[0] < self.reset_button.get_rect().right and event.pos[1] > Window.WINDOW_HEIGHT - Window.FONT_SIZE and event.pos[1] < Window.WINDOW_HEIGHT:
                    # reset button clicked
                    self.atom = Atom(self, 0, 0, 0)
                    self.update()
                elif event.pos[0] > 375 and event.pos[0] < Window.WINDOW_WIDTH and event.pos[1] > 0 and event.pos[1] < 25:
                    if self.do_radioactivity:
                        self.do_radioactivity = False
                    else:
                        self.do_radioactivity = True
        if self.do_radioactivity:
            if self.atom.try_decay():
                print("Decaying.")
                if self.atom.neutrons == self.atom.protons:
                    print("Emitting a helium nucleus.")
                    self.atom = Atom(self, self.atom.protons - 2, self.atom.neutrons - 2, self.atom.electrons - 2)
                # beta plus decay
                elif self.atom.protons > self.atom.neutrons:
                    print("Turning a proton into a neutron.")
                    self.atom = Atom(self, self.atom.protons - 1, self.atom.neutrons + 1, self.atom.electrons - 1)
                # beta minus decay
                else:
                    print("Turning a neutron into a proton.")
                    self.atom = Atom(self, self.atom.protons + 1, self.atom.neutrons - 1, self.atom.electrons - 1)
                self.update()

    def load_images(self):
        try:
            self.proton_image = open('proton.bmp', 'r')
            self.neutron_image = open('neutron.bmp', 'r')
            self.electron_image = open('electron.bmp', 'r')
        except IOError:
            print("Could not find one of these files: proton.gif, neutron.gif, electron.gif. They should be in the same folder as atombuilder.py.")

Window()
