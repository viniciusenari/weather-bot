from project.config import auth_multi, auth_token, personalization_id, twid, bearer, csrf_token
import requests

class Twitter:
    def __init__(self):
        self.cookies = {
            'guest_id_marketing': 'v1%3A167227742656414483',
            'guest_id_ads': 'v1%3A167227742656414483',
            'kdt': 'GX8dj5TH1kntwy8OkV3MaYhXmpk85CDG3e24lM0t',
            'night_mode': '1',
            'at_check': 'true',
            'lang': 'en',
            'co': 'br',
            'dnt': '1',
            'ads_prefs': '"HBISAAA="',
            'auth_multi': auth_multi,
            'auth_token': auth_token,
            'personalization_id': personalization_id,
            'guest_id': 'v1%3A167536075737167880',
            'twid': twid,
            'ct0': csrf_token,
        }

        self.headers = {
            'authority': 'api.twitter.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.6',
            'authorization': f'Bearer {bearer}',
            'content-type': 'application/json',
            'origin': 'https://twitter.com',
            'referer': 'https://twitter.com/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Brave";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'x-csrf-token': csrf_token,
            'x-twitter-active-user': 'yes',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-twitter-client-language': 'en',
        }

        self.json_data = {
            'variables': {
                'tweet_text': '',
                'dark_request': False,
                'media': {
                    'media_entities': [],
                    'possibly_sensitive': False,
                },
                'withDownvotePerspective': False,
                'withReactionsMetadata': False,
                'withReactionsPerspective': False,
                'withSuperFollowsTweetFields': True,
                'withSuperFollowsUserFields': True,
                'semantic_annotation_ids': [],
            },
            'features': {
                'longform_notetweets_consumption_enabled': True,
                'tweetypie_unmention_optimization_enabled': True,
                'vibe_api_enabled': True,
                'responsive_web_edit_tweet_api_enabled': True,
                'graphql_is_translatable_rweb_tweet_is_translatable_enabled': True,
                'view_counts_everywhere_api_enabled': True,
                'interactive_text_enabled': True,
                'responsive_web_text_conversations_enabled': False,
                'responsive_web_twitter_blue_verified_badge_is_enabled': True,
                'verified_phone_label_enabled': False,
                'standardized_nudges_misinfo': True,
                'tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled': False,
                'responsive_web_graphql_timeline_navigation_enabled': True,
                'responsive_web_enhance_cards_enabled': False,
            },
            'queryId': 'uDKNAYFNOggQWtel6bilRw',
        }

    def post_tweet(self, text):
        self.json_data['variables']['tweet_text'] = text

        requests.post(
            'https://api.twitter.com/graphql/uDKNAYFNOggQWtel6bilRw/CreateTweet',
            cookies=self.cookies,
            headers=self.headers,
            json=self.json_data,
        )