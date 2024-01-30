/** @type {import('next').NextConfig} */
const nextConfig = {};

export default nextConfig;

// // フロントエンドとバックエンドを疎通させるための設定
// module.exports = {
//     async rewrites() {
//         return [
//             {
//                 source:'/api/:path*',
//                 destination: 'http://host.docker.internal:8000/api/:path*/',
//             },
//         ]
//     },
// };
