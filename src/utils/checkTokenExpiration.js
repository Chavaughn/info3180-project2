import jwtDecode from 'jwt-decode';
import router from './router';

export function checkTokenExpiration() {
  const token = localStorage.getItem('JWT');

  if (!token) {
    router.push('/login');
    return;
  }

  const decodedToken = jwtDecode(token);

  if (decodedToken.exp * 1000 < Date.now()) {
    // Token is expired, redirect to login page
    localStorage.removeItem('JWT');
    localStorage.removeItem('user_id');
    router.push('/login');
    return;
  }
}
