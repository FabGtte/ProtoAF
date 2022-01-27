from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Exoplanet, Star
import json
import requests

def getexoclockdata(request):

    allexoplanets = {}
    if request.GET.get('mybutton') == 'Click':
        url = 'https://www.exoclock.space/database/planets_json'
        exoclock_response = requests.get(url)
        serialized_exoclockdata = exoclock_response.json()
        

        for planet, planetdata in serialized_exoclockdata.items(): 
                exoplanet_API = Exoplanet(
                    name = planetdata['name'],
                    type = '',
                    priority = planetdata['priority'],
                    total_observations = planetdata['total_observations'],
                    recent_observations = planetdata ['recent_observations'],
                    ra_j2000 = planetdata['ra_j2000'],
                    dec_j2000 = planetdata['dec_j2000'],
                    v_mag = planetdata['v_mag'],
                    r_mag = planetdata['r_mag'],
                    gaia_g_mag = planetdata['gaia_g_mag'],
                    depth_mmag = planetdata['depth_mmag'],
                    transit_duration_hours = planetdata['duration_hours'],
                    ephemeris_mid_time_bjd_tdb = planetdata['t0_bjd_tdb'],
                    ephemeris_mid_time_uncertainty = planetdata['t0_unc'],
                    ephemeris_period_days = planetdata['period_days'],
                    ephemeris_period_uncertainty = planetdata['period_unc'],
                    ephemeris_current_oc_min = planetdata['current_oc_min']
                )

                if Exoplanet.objects.filter(name=exoplanet_API.name).exists(): 
                    continue
                else: 
                    exoplanet_API.save()

        allexoplanets = Exoplanet.objects.all().order_by('name')

    return render(request, 'infoplanets.html', {'exoplanets' : list(allexoplanets)})

def getnasadata(request):

    if request.GET.get('mybutton')=='Click':
        url = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+ps&format=json'
        nasa_response = requests.get(url)
        serialized_nasadata = nasa_response.json()

        for star, stardata in serialized_nasadata.items():
            if Exoplanet.objects.filter(name=stardata.pl_name).exists():
                hoststar_API = Star(
                    name = stardata['hostname'],
                    ra = stardata['ra'],
                    dec = stardata['dec'],
                    stellar_distance = stardata['sy_dist'],
                    parallax = stardata['sy_plx'],
                    parallax_err = stardata['sy_plxerr1'],
                    ecliptic_latitude = stardata['elat'],
                    ecliptic_longiude = stardata['elon'],
                    galactic_latitude = stardata['glat'],
                    galactic_longitude = stardata['glon'],
                    orbiting_planets = stardata[''],
                    total_proper_motion = stardata['sy_pm'],
                    total_proper_motion_err = stardata['sy_pmerr1'],
                    proper_motion_ra = stardata['sy_pmra'],
                    proper_motion_ra_err = stardata['sy_pmraerr1'],
                    proper_motion_dec = stardata['sy_pmdec'],
                    proper_motion_dec_err = stardata['sy_pmdecerr1'],
                    effective_temperature = stardata['st_teff'],
                    effective_temperature_err = stardata['st_tefferr1'],
                    spectral_type = stardata['st_spectype'],
                    metallicity = stardata['st_met'],
                    metallicity_err = stardata['st_meterr1'],
                    density = stardata['st_dens'],
                    density_err = stardata['st_denserr1'],
                    mass = stardata['st_mass'],
                    mass_err = stardata['st_masserr1'],
                    radius = stardata['st_rad'],
                    radius_err = stardata['st_raderr1'],
                    surface_gravity = stardata['st_logg'],
                    surface_gravity_err = stardata['st_loggerr1'],
                    luminosity = stardata['st_lum'],
                    luminosity_err = stardata['st_lumerr1'],
                    radial_velocity = stardata['st_radv'],
                    radial_velocity_err = stardata['st_radverr1'],
                    age = stardata['st_age'],
                    age_err = stardata['st_ageerr1'],
                    rotational_velocity = stardata['st_vsin'],
                    rotational_velocity_err = stardata['st_vsinerr1'],
                    rotation_period = stardata['st_rotp'],
                    rotation_period_err = stardata['st_rotperr1'],

                    #Photometry
                    bmag = stardata['sy_bmag'],
                    bmag_err =stardata['sy_bmagerr1'],
                    gmag = stardata['sy_gmag'],
                    gmag_err = stardata['sy_gmagerr1'],
                    gaiamag = stardata['sy_gaiamag'],
                    gaiamag_err = stardata['sy_gaiamagerr1'],
                    hmag = stardata['sy_hmag'],
                    hmag_err = stardata['sy_hmagerr1'],
                    imag = stardata['sy_imag'],
                    imag_err = stardata['sy_imagerr1'],
                    jmag = stardata['sy_jmag'],
                    jmag_err = stardata['sy_jmagerr1'],
                    kmag = stardata['sy_kmag'],
                    kmag_err = stardata['sy_kmagerr1'],
                    rmag = stardata['sy_rmag'],
                    rmag_err = stardata['sy_rmagerr1'],
                    vmag = stardata['sy_vmag'],
                    vmag_err = stardata['sy_vmagerr1'],
                    tmag = stardata['sy_tmag'],
                    tmag_err = stardata['sy_tmagerr1'],
                    w1mag = stardata['sy_w1mag'],
                    w1mag_err = stardata['sy_w1magerr1'],
                    w2mag = stardata['sy_w2mag'],
                    w2mag_err = stardata['sy_w2magerr1'],
                    w3mag = stardata['sy_w3mag'],
                    w3mag_err = stardata['sy_w3magerr1'],
                    w4mag = stardata['sy_w4mag'],
                    w4mag_err = stardata['sy_w4magerr1'],
                        )
                
            else: continue

def show_exopl_info(request, exoplanet_name):

    exoplanet = Exoplanet.objects.get(name=exoplanet_name)
    return render(request, 'exoplanet.html', {'exoplanet': exoplanet})


def planetTypeFilter(request):

    #if request.GET.get('plTypeCheckbox') == 'Checked' & request.GET.get('submitbutton') == 'Submit':
     #   QuerySet = Exoplanet.objects.all().filter(type)

    return render(request, 'exoplanets.html', )


def search_planet(request):

    if request.method == 'POST':
        searched = request.POST['searched']
        exoplanet = Exoplanet.objects.filter(name__icontains = searched)
        print(searched)
        print(exoplanet)

        return render(request, 'search_planet.html', {'searched': searched, 'exoplanet': exoplanet})


def is_it_json(serialized_exoclockdata):
    try:
        json.loads(serialized_exoclockdata)
    except ValueError as nope:
        return False
    return True

def checker(request):
    jsonbooleanchecker = 'No info'
    if is_it_json == True:
        jsonbooleanchecker = 'JSON'
    if is_it_json == False: 
        jsonbooleanchecker = 'Not a JSON'

    return render(request, 'infoplanets.html', {'isitajson' : jsonbooleanchecker})

    




