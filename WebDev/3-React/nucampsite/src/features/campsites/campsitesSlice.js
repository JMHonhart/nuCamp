import { CAMPSITES } from '../../app/shared/CAMPSITES';

export const selectAllCampsites = () => {
    return CAMPSITES;
};

export const selectedCampsiteById = (id) => {
    return CAMPSITES.find((campsite) => campsite.id === id);
};